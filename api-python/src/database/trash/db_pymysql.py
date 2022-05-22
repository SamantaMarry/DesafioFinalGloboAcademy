import os
import pymysql


class db_pymysql:
    def __init__(self) -> None:
        self.__conn = None
        # self.__cursor = None
        self.__open_connection()

    # --
    def __open_connection(self):
        try:
            if self.__conn is None:
                self.__conn = pymysql.connect(
                    host=os.getenv("DB_HOST"),
                    port=3306,
                    user=os.getenv("DB_USERNAME"),
                    passwd=os.getenv("DB_PASSWORD"),
                    db=os.getenv("DB_DATABASE"),
                    cursorclass=pymysql.cursors.DictCursor,
                )
                # self.__cursor = self.__conn.cursor()

        except pymysql.MySQLError as sqle:
            raise pymysql.MySQLError(
                f"Failed to connect to the database due to: {sqle}"
            )
        except Exception as e:
            raise Exception(f"An exception occured due to: {e}")

    def pquey(self, query, args=None):
        try:
            if not query or not isinstance(query, str):
                raise Exception()

            if not self.__conn:
                self.__open_connection()

            with self.__conn.cursor() as cursor:
                cursor.execute(query, args)
                if "SELECT" in query.upper():
                    result = cursor.fetchall()
                else:
                    self.__conn.commit()
                    result = f"{cursor.rowcount} row(s) affected."
                cursor.close()

                return result
        except pymysql.MySQLError as sqle:
            raise pymysql.MySQLError(f"Failed to execute query due to: {sqle}")
        except Exception as e:
            raise Exception(f"An exception occured due to: {e}")
