import os
import mysql.connector
from mysql.connector import errorcode


class db_mysql:
    def __init__(self) -> None:
        self.__conn = None
        self.__open_connection()

    # --
    def __open_connection(self):
        try:
            if self.__conn is None:
                self.__conn = mysql.connector.connect(
                    host=os.getenv("DB_HOST"),
                    user=os.getenv("DB_USERNAME"),
                    password=os.getenv("DB_PASSWORD"),
                    database=os.getenv("DB_DATABASE"),
                )
                # self.__cursor = self.__conn.cursor(dictionary=True)

        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database doesn't exist")
            elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("User name or password is wrong")
            else:
                print(error)

    def pquey(self, query, args=None):
        try:
            if not query or not isinstance(query, str):
                raise Exception()

            # if not self.__conn or not self.__conn.is_connected():
            #     self.__open_connection()

            self.__conn.reconnect()

            with self.__conn.cursor(dictionary=True, buffered=True) as cursor:
                cursor.execute(query, args)
                if "SELECT" in query.upper():
                    result = cursor.fetchall()
                else:
                    self.__conn.commit()
                    result = f"{cursor.rowcount} row(s) affected."
                cursor.close()

                return result
        except Exception as e:
            raise Exception(f"An exception occured due to: {e}")
