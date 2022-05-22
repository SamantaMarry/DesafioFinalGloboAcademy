# import os

# from src.database.db_sqlite3 import db_sqlite3

# # from src.database.db_mysql import db_mysql
# from src.database.db_mysql import db_mysql

# # from src.database.db_pymysql import db_pymysql

# # from src.database.db_mysql2 import db_mysql2

# if os.getenv("DB_DIALECT") == "mysql":
#     db = db_mysql()
# else:
#     db = db_sqlite3()

db = None
