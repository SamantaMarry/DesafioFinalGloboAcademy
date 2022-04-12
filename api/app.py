from src.server.instance import server
from src.server.db import db

app = server.app


# @app.before_first_request
# def create_table():
#     db.create_all()

db.sql_create_db()

if __name__ == "__main__":
    server.run()
