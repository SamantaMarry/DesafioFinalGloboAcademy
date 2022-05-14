import os
from flask import request

from flask_restful import Resource, reqparse
from marshmallow import ValidationError

from src.server.instance import server

from src.database import data_base
from src.model.restaurant import RestaurantModel
from src.model.product import ProductModel

from src.controllers.dto.restaurant_dto import (
    RestaurantDtoMarshmallow,
    RestaurantDtoRestfull,
)

api = server.api

# ----------------

# https://marshmallow.readthedocs.io/en/stable/extending.html
# https://stackoverflow.com/questions/65830811/marshmallow-for-python-giving-valueerror-not-enough-values-to-unpack-expected
# https://github.com/marshmallow-code/marshmallow/issues/1130
# https://stackoverflow.com/questions/63944416/marshmallow-custom-validation-message-for-email
# https://stackoverflow.com/questions/66290964/marshmallow-not-returning-validation-errors-from-a-nested-list
# https://www.youtube.com/watch?v=dmnOf-VvJcU


class RestaurantController(Resource):
    @classmethod
    def routes(self):
        api.add_resource(
            RestaurantProductList, "/restaurants/<int:id_restaurant>/product"
        )
        api.add_resource(Restaurant, "/restaurants/<int:id>")
        api.add_resource(RestaurantList, "/restaurants")


class Restaurant(Resource):
    def get(self, id):
        db = data_base.get_connect("db")

        restaurant = RestaurantModel.find_by_id(db, id)
        if not restaurant:
            return {}, 204

        return restaurant

    def put(self, id):
        db = data_base.get_connect("db")
        restaurant = RestaurantModel.find_by_id_build(db, id)
        if not restaurant:
            return None, 204

        # --
        parser = reqparse.RequestParser()
        parser.add_argument(
            "name", type=str, required=True, help="Name cannot be blank"
        )
        parser.add_argument(
            "address", type=str, required=True, help="Address cannot be blank"
        )
        parser.add_argument("description", type=str, required=False)
        parser.add_argument(
            "url_image", type=str, required=True, help="url_image cannot be blank"
        )
        parser.add_argument(
            "responsible_name",
            type=str,
            required=True,
            help="responsible_name cannot be blank",
        )
        data = parser.parse_args()
        # --

        # update
        restaurant.name = data.name
        restaurant.address = data.address
        restaurant.description = data.description
        restaurant.url_image = data.url_image
        restaurant.responsible_name = data.responsible_name

        try:
            restaurant.update()
            db.commit()
        except Exception as error:
            db.rollback()
            return {"Error": str(error)}, 400

        return None, 200, {"Location": f"{os.getenv('ROOT_URL')}/restaurants/{id}"}

    def delete(self, id):
        db = data_base.get_connect("db")
        restaurant = RestaurantModel.find_by_id_build(db, id)
        if not restaurant:
            return {}, 204

        try:
            restaurant.delete()
            db.commit()
        except Exception as error:
            db.rollback()
            return {"Error": str(error)}, 400

        return restaurant.to_dict(), 200


class RestaurantList(Resource):
    def get(self):
        db = data_base.get_connect("db")

        # querystring
        order = request.args.get("order", default="", type=str)

        try:
            restaurants = RestaurantModel.find_all(db, order=order)
        except Exception as error:
            return {"Error": str(error)}, 400

        return restaurants

    def post2(self):
        try:
            restaurant_schema = RestaurantDtoMarshmallow()
            req = restaurant_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 422

        print(req)
        return {}, 200

    def post(self):
        data = RestaurantDtoRestfull().getArgs()

        db = data_base.get_connect("db")
        restaurant = RestaurantModel(db).build(
            data.name,
            data.address,
            data.description,
            data.url_image,
            data.responsible_name,
        )

        try:
            with db.query_area(commit=True):
                lastid = restaurant.insert().last_id
        except Exception as error:
            return {"Error": str(error)}, 400

        return None, 201, {"Location": f"{os.getenv('ROOT_URL')}/restaurants/{lastid}"}


class RestaurantProductList(Resource):
    def get(self, id_restaurant):
        db = data_base.get_connect("db")

        order = request.args.get("order", default="", type=str)
        try:
            products = ProductModel.find_all_prodcts_restaurant_id(
                db, id_restaurant, order=order
            )
        except Exception as error:
            return {"Error": str(error)}, 400
        return products
