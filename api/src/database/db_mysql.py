from contextlib import contextmanager
import mysql.connector
from mysql.connector import errorcode


class db_mysql:
    def __init__(self, host, user, password, database) -> mysql.connector:
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database
        self.__conn = None
        self.__cursor = None
        self.__open_connection()

    def __open_connection(self):

        try:
            if self.__conn is None:
                self.__conn = mysql.connector.connect(
                    host=self.__host,
                    user=self.__user,
                    password=self.__password,
                    database=self.__database,
                )

                # https://stackoverflow.com/questions/46682012/what-is-a-mysql-buffered-cursor-w-r-t-python-mysql-connector
                # buffered=True
                self.__cursor = self.__conn.cursor(dictionary=True)

            # print(f"self.__conn {self.__conn}")

        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database doesn't exist")
            elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("User name or password is wrong")
            else:
                print(error)

    def __del__(self) -> None:
        self.__conn.close()

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

    @property
    def fetchone(self):
        return self.__cursor.fetchone()

    @property
    def fetchall(self):
        return self.__cursor.fetchall()

    @property
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
        except mysql.connector.Error as err:
            print("DatabaseError {} ".format(err))
            self.rollback()
            raise err
        else:
            if commit:
                self.commit()
        # finally:
        #     self.__cursor.close()

    def pquery(self, query, args=None):
        try:
            if not query or not isinstance(query, str):
                raise Exception("Query should be string")

            self.__cursor.execute(query, args)
            # print("Last Query: {}".format(self.__cursor.statement))

            return self

        except Exception as e:
            raise Exception(
                # cursor.fetchwarnings()
                f"An exception occured due to: {e} \r\n Last Query: {self.__cursor.statement}"
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
            parms_bind.append("%s")
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
            fields.append(f"{field} = %s")
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
