from dotenv import load_dotenv
from src.database import data_base

load_dotenv()

from src.server.instance import server
from flask_pydantic_spec import FlaskPydanticSpec


from src.controllers.restaurants import RestaurantController
from src.controllers.products import ProductController

app = server.app


@app.before_request
def before_request_func():
    # connect data base env
    data_base.connect("db")


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
