# https://stackoverflow.com/questions/3783238/python-database-connection-close
# https://stackoverflow.com/questions/38076220/python-mysqldb-connection-in-a-class/38078544#38078544
# https://stackoverflow.com/questions/6114064/python-and-mysql-connection-problems-mysqldb-api

import os
from flask import g  # https://flask.palletsprojects.com/en/2.1.x/appcontext/
from src.database.db_mysql import db_mysql
from src.database.db_sqlite3 import db_sqlite3


def connect(alias, database=None, dialect=None, host=None, user=None, password=None):

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

    add_connect(alias, db)

    return db


# utilizando contexto para fazer a gestão das conexões com o banco e dados
# durante a requisição
def get_connect(alias):
    return g._db_connects.get(alias)


def get_connects():
    return g._db_connects


def add_connect(alias, db):
    if "_db_connects" not in g:
        g._db_connects = {}
    g._db_connects[alias] = db


def close_connects():
    # https://pt.stackoverflow.com/questions/151176/iterando-sobre-dicion%C3%A1rios-aninhados-pyth%C3%B4nico
    # http://devfuria.com.br/python/dicionarios-dictionaries/
    if "_db_connects" in g:
        for connect in g._db_connects:
            g._db_connects[connect].close_connect()
