import os
from flask import request
from flask_restful import Resource, reqparse

from src.server.instance import server
from src.database import data_base
from src.model.product import ProductModel
from src.model.restaurant import RestaurantModel
from src.controllers.dto.product_dto import (
    # ProductDtoMarshmallow,
    ProductDtoRestfull,
)


api = server.api


class ProductController(Resource):
    @classmethod
    def routes(self):
        api.add_resource(Product, "/products/<int:id>")
        api.add_resource(ProductList, "/products")


class Product(Resource):
    def get(self, id):
        db = data_base.get_connect("db")
        product = ProductModel.find_by_id(db, id)
        if not product:
            return {}, 204

        return product

    def put(self, id):
        db = data_base.get_connect("db")
        data = ProductDtoRestfull().getArgs()

        product = ProductModel.find_by_id_build(db, id)
        if not product:
            return None, 204

        restaurant = RestaurantModel.find_by_id(db, data.id_restaurant)
        if not restaurant:
            return {"Error": "Restaurant not exist"}, 404

        product.name = data.name
        product.url_image = data.url_image
        product.description = data.description
        product.price = data.price
        product.id_restaurant = data.id_restaurant

        try:
            product.update()
            db.commit()
        except Exception as error:
            db.rollback()
            return {"Error": str(error)}, 400

        return None, 200, {"Location": f"{os.getenv('ROOT_URL')}/products/{id}"}

    def delete(self, id):
        db = data_base.get_connect("db")
        product = ProductModel.find_by_id_build(db, id)
        if not product:
            return {}, 204

        try:
            product.delete()
            db.commit()
        except Exception as error:
            db.rollback()
            return {"Error": str(error)}, 400

        return product.to_dict(), 200


class ProductList(Resource):
    def get(self):
        db = data_base.get_connect("db")

        # querystring
        order = request.args.get("order", default="", type=str)

        try:
            products = ProductModel.find_all(db, order=order)
        except Exception as error:
            return {"Error": str(error)}, 400
        return products

    def post(self):
        db = data_base.get_connect("db")
        data = ProductDtoRestfull().getArgs()

        print(data)

        restaurant = RestaurantModel.find_by_id(db, data.id_restaurant)
        if not restaurant:
            return {"Error": "Restaurant not exist"}, 404

        product = ProductModel(db).build(
            data.name,
            data.url_image,
            data.description,
            data.price,
            data.extras,
            data.id_restaurant,
        )

        try:
            lastid = product.insert().last_id
            db.commit()
        except Exception as error:
            db.rollback()
            return {"Error": str(error)}, 400

        return None, 201, {"Location": f"{os.getenv('ROOT_URL')}/products/{lastid}"}