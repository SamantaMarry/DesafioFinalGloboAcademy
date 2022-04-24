from dotenv import load_dotenv
from flask import g
from src.database.data_base import data_base

# from src.database.db_connect import db

load_dotenv()

from src.server.instance import server
from flask_pydantic_spec import FlaskPydanticSpec


from src.controllers.restaurants import RestaurantController
from src.controllers.products import ProductController

app = server.app


# @app.before_request
# def before_func():
#     # g._db_connects = []
#     print("-- before_request -- ")


@app.after_request
def after_request_func(response):
    data_base.close_connects()
    return response


# @app.before_first_request
# def create_table():
#     db.sql_create_db()

spec = FlaskPydanticSpec("FlaskPydanticSpec", title="JasonsFood")
spec.register(app)

RestaurantController.routes()
ProductController.routes()

if __name__ == "__main__":
    server.run()
