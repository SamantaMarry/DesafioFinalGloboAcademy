import os
from flask import g  # https://flask.palletsprojects.com/en/2.1.x/appcontext/
from src.database.db_mysql import db_mysql
from src.database.db_mysql import db_mysql
from src.database.db_sqlite3 import db_sqlite3


class data_base:
    @classmethod
    def connect(cls, database=None, dialect=None, host=None, user=None, password=None):

        # if empty, load info .env
        database = os.getenv("DB_DATABASE") if not database else database
        dialect = os.getenv("DB_DIALECT") if not dialect else dialect
        host = os.getenv("DB_HOST") if not host else host
        user = os.getenv("DB_USERNAME") if not user else user
        password = os.getenv("DB_PASSWORD") if not password else password

        match dialect:
            case "mysql":
                db = db_mysql(host, user, password, database)
            case "sqlite3":
                db = db_sqlite3(database)
            case _:
                # default
                db = db_sqlite3(database)

        cls.add_connect(db)

        return db

    # utilizando contexto para fazer a gestão das conexões com o banco e dados
    @classmethod
    def get_connects(cls):
        return g._db_connects

    @classmethod
    def add_connect(cls, db):
        if "_db_connects" not in g:
            g._db_connects = []
        g._db_connects.append(db)

    @classmethod
    def close_connects(cls):
        if "_db_connects" in g:
            for connect in g._db_connects:
                connect.close_connect()
