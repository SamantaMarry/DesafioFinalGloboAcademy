from dotenv import load_dotenv

load_dotenv()

from src.server.instance import server
from src.server.db import db
from flask_pydantic_spec import FlaskPydanticSpec


from src.controllers.restaurants import RestaurantController
from src.controllers.products import ProductController

app = server.app


@app.before_first_request
def create_table():
    db.sql_create_db()

# only create database
# db.sql_create_db()

spec = FlaskPydanticSpec("FlaskPydanticSpec", title="JasonsFood")
spec.register(app)

RestaurantController.routes()
ProductController.routes()

if __name__ == "__main__":
    server.run()
