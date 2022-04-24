import sqlite3
from sqlite3 import Error

# https://docs.python.org/3.8/library/sqlite3.html#sqlite3.Connection.set_trace_callback
# https://www.digitalocean.com/community/tutorials/how-to-use-the-sqlite3-module-in-python-3
# https://www.tutorialspoint.com/sqlite/sqlite_python.htm
# https://zetcode.com/python/sqlite/
# https://likegeeks.com/python-sqlite3-tutorial/#:~:text=To%20use%20SQLite3%20in%20Python,us%20execute%20the%20SQL%20statements.&text=That%20will%20create%20a%20new,db'.
class db_sqlite3:
    def __init__(self, database):
        self.__database = database
        self.__conn = None
        self.__cursor = None
        self.__open_connection()

    def __open_connection(self):

        try:
            if self.__conn is None:
                self.__conn = sqlite3.connect(
                    f"{self.__database}.db", check_same_thread=False
                )
                self.__conn.row_factory = self.dict_factory

                self.__conn.row_factory = self.dict_factory
                self.__cursor = self.__conn.cursor()

        except sqlite3.Error as err:
            print("Sql error: %s" % (" ".join(err.args)))
            print("Exception class is: ", err.__class__)

    # Convert query result in dictionary
    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def __del__(self) -> None:
        self.__conn.close()

    def pquey(self, query, args=[]):
        query = query.replace(f"%s", "?")
        try:
            if not query or not isinstance(query, str):
                raise Exception("Query should be string")

            if not self.__conn:
                self.__open_connection()

            self.__cursor.execute(query, args)

            # print("Last Query: {}".format(self.__cursor.statement))

            return self

        except Exception as e:
            raise Exception(
                # cursor.fetchwarnings()
                f"An exception occured due to: {e}"
            )

    def get_cursor(self):
        return self.__cursor

    def pquey_result(self, query, args=None):
        self.pquey(query, args)
        return self.fetchall()

    def fetchone(self):
        return self.__cursor.fetchone()

    def fetchall(self):
        return self.__cursor.fetchall()

    def fetchmany(self, size=None):
        return self.__cursor.fetchmany(size)

    def last_id(self):
        return self.__cursor.lastrowid

    def rollback(self):
        return self.__conn.rollback()

    def commit(self):
        return self.__conn.commit()

    # def close_cursor(self) -> None:
    #     self.__cursor.close()

    def close_connect(self) -> None:
        self.__conn.close()

    def insert(self, table, values):
        fields = []
        parms_bind = []
        args = []
        for field, value in values.items():
            fields.append(field)
            parms_bind.append("%s")
            args.append(value)

        # ','.join(str(v) for v in fields)
        fields_insert = ", ".join(fields)
        binds_insert = ", ".join(parms_bind)

        sql = f"""
            INSERT INTO {table} ({fields_insert})
            VALUES ({binds_insert})
        """
        res = self.pquey(sql, args)

        return res

    def update(self, table, values, where, args=[]):
        fields = []
        args_values = []
        for field, value in values.items():
            fields.append(f"{field} = %s")
            args_values.append(value)

        fields_insert = ", ".join(fields)
        args = args_values + args

        sql = f"""
            UPDATE {table} SET {fields_insert}
            WHERE 1=1 AND {where}
        """

        res = self.pquey(sql, args)
        return res

    def delete(self, table, where, args=[]):
        sql = f"""
            DELETE FROM {table}
            WHERE 1=1 AND {where}
        """
        res = self.pquey(sql, args)

        return res
