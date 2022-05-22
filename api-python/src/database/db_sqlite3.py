import sqlite3
from sqlite3 import Error
from contextlib import contextmanager


class db_sqlite3:
    def __init__(self, database) -> sqlite3:
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

    def __del__(self) -> None:
        self.__conn.close()

    # Convert query result in dictionary
    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    @property
    def get_connection(self):
        return self.__conn

    @property
    def get_cursor(self):
        return self.__cursor

    # def close_cursor(self) -> None:
    #     self.__cursor.close()

    def close_connect(self) -> None:
        self.__conn.close()

    ###################
    ### TRANSACTION ###
    ###################

    def fetchone(self):
        return self.__cursor.fetchone()

    def fetchall(self):
        return self.__cursor.fetchall()

    def fetchmany(self, size=None):
        return self.__cursor.fetchmany(size)

    @property
    def last_id(self):
        return self.__cursor.lastrowid

    ###################
    ### TRANSACTION ###
    ###################

    def rollback(self):
        return self.__conn.rollback()

    def commit(self):
        return self.__conn.commit()

    #####################
    ### EXECUTE QUERY ###
    #####################

    @contextmanager
    def query_area(self, commit: bool = False):
        """
        A context manager style of using a DB cursor for database operations.
        This function should be used for any database queries or operations that
        need to be done.

        :param commit:
        A boolean value that says whether to commit any database changes to the database. Defaults to False.
        :type commit: bool
        """
        # cursor = self.get_cursor()
        try:
            yield self
        except sqlite3.Error as err:
            print("DatabaseError {} ".format(err))
            self.rollback()
            raise err
        else:
            if commit:
                self.commit()
        # finally:
        #     self.__cursor.close()

    def pquery(self, query, args=[]):
        query = query.replace(f"%s", "?")
        try:
            if not query or not isinstance(query, str):
                raise Exception("Query should be string")

            self.__cursor.execute(query, args)
            # print("Last Query: {}".format(self.__cursor.statement))

            return self

        except Exception as e:
            raise Exception(
                # cursor.fetchwarnings()
                # f"An exception occured due to: {e} \r\n Last Query: {self.__cursor.statement}"
                f"An exception occured due to: {e} \r\n Last Query: ???"
            )

    def pquery_result(self, query, args=None):
        self.pquery(query, args)
        return self.fetchall()

    ###################
    ### ACTIONS SQL ###
    ###################

    def sql_table_insert(self, table: str, values: dict, commit: bool = False):
        fields = []
        parms_bind = []
        args = []
        for field, value in values.items():
            fields.append(field)
            parms_bind.append("?")
            args.append(value)

        # ','.join(str(v) for v in fields)
        fields_insert = ", ".join(fields)
        binds_insert = ", ".join(parms_bind)

        sql = f"""
            INSERT INTO {table} ({fields_insert})
            VALUES ({binds_insert})
        """
        self.pquery(sql, args)

        if commit:
            self.commit()

        return self

    def sql_table_update(
        self, table: str, values: dict, where, args: list = [], commit: bool = False
    ):
        fields = []
        args_values = []
        for field, value in values.items():
            fields.append(f"{field} = ?")
            args_values.append(value)

        fields_insert = ", ".join(fields)
        args = args_values + args

        sql = f"""
            UPDATE {table} SET {fields_insert}
            WHERE 1=1 AND {where}
        """

        self.pquery(sql, args)

        if commit:
            self.commit()

        return self

    def sql_table_delete(
        self, table: str, where: dict, args: list = [], commit: bool = False
    ):
        sql = f"""
            DELETE FROM {table}
            WHERE 1=1 AND {where}
        """
        self.pquery(sql, args)

        if commit:
            self.commit()

        return self
