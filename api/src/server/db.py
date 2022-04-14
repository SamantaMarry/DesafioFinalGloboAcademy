import os
from src.database.db_sqlite3 import db_sqlite3
from src.database.db_mysql import db_mysql

if os.getenv("DB_DIALECT") == "mysql":
    db = db_mysql()
else:
    db = db_sqlite3()
