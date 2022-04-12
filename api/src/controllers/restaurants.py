import os
from flask import request
from flask_restful import Resource, reqparse
from src.server.instance import server
from src.server.db import db
from src.model.restaurant import RestaurantModel

api = server.api


class RestaurantController(Resource):
    @classmethod
    def routes(self):
        api.add_resource(Restaurant, "/restaurants/<int:id>")
        api.add_resource(RestaurantList, "/restaurants")


class Restaurant(Resource):
    def get(self, id):
        RestaurantModel.setConnectDataBase(db)
        RestaurantModel.setConnectDataBase(db)
        restaurant = RestaurantModel.find_by_id(id)
        if not restaurant:
            return {}, 204

        return restaurant

    def put(self, id):
        RestaurantModel.setConnectDataBase(db)
        restaurant = RestaurantModel.find_by_id_build(id)
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
            restaurant.update().lastrowid
        except Exception as error:
            return {"Error": str(error)}, 400

        return None, 200, {"Location": f"{os.getenv('ROOT_URL')}/restaurants/{id}"}

    def delete(self, id):
        RestaurantModel.setConnectDataBase(db)
        restaurant = RestaurantModel.find_by_id_build(id)
        if not restaurant:
            return {}, 204

        restaurant.delete()
        return restaurant.to_dict(), 200


class RestaurantList(Resource):
    def get(self):
        RestaurantModel.setConnectDataBase(db)

        # querystring
        order = request.args.get("order", default="", type=str)

        try:
            restaurants = RestaurantModel.find_all(order=order)
        except Exception as error:
            return {"Error": str(error)}, 400
        return restaurants

    def post(self):
        RestaurantModel.setConnectDataBase(db)

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

        restaurant = RestaurantModel().build(
            data.name,
            data.address,
            data.description,
            data.url_image,
            data.responsible_name,
        )

        print()

        try:
            lastid = restaurant.insert().lastrowid
        except Exception as error:
            return {"Error": str(error)}, 400
        # os.getenv("ROOT_URL")
        return None, 201, {"Location": f"{os.getenv('ROOT_URL')}/restaurants/{lastid}"}
