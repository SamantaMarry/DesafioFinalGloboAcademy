from dotenv import load_dotenv

load_dotenv()

from src.server.instance import server
from src.server.db import db

from src.controllers.restaurants import RestaurantController
from src.controllers.products import ProductController

app = server.app


# @app.before_first_request
# def create_table():
#     db.create_all()
# db.sql_create_db()

RestaurantController.routes()
ProductController.routes()

if __name__ == "__main__":
    server.run()
