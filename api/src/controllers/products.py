from flask_restful import Resource, reqparse
from src.server.instance import server
from src.model.product import ProductModel
from src.server.db import db

api = server.api

class ProductController(Resource):
    @classmethod
    def routes(self):
        api.add_resource(Product, "/products/<int:id>")
        api.add_resource(ProductList, "/products")
 
class Product(Resource):
    def get(self, id):
        print('Product GET \o/ {}'.format(id))

    def put(self, id):
        print('Product PUT \o/ {}'.format(id))

    def delete(self, id):
        print('Product DELETE \o/ {}'.format(id))

class ProductList(Resource):
    def get(self):
       print('ProductList GET \o/')

    def post(self):
        ProductModel.setConnectDataBase(db)
        print('ProductList POST \o/')

        ###
        # request
        parser = reqparse.RequestParser()
        parser.add_argument(
            "name", type=str, required=True, help="name cannot be blank"
        )
        parser.add_argument(
            "url_image", type=str, required=True, help="url_image cannot be blank"
        )
        parser.add_argument(
            "description", type=str, required=False
        )
        parser.add_argument(
            "price", type=float, required=True, help="price cannot be blank"
        )
        parser.add_argument(
            "extras", type=str, required=False
        )
        parser.add_argument(
            "id_restaurants", type=int, required=False, help="One restaurant should be informed"
        )
        data = parser.parse_args()
        ###

        product = ProductModel().build(
            data.name, data.url_image, data.description, data.price, data.extras, data.id_restaurants
        )

        try:
            lastid = product.insert().lastrowid
        except Exception as error:
            return {"Error": str(error)}, 400

        # return None, 201, {"Location": f"http://127.0.0.1:5000/movies/{lastid}"}

#   id TEXT AUTOINCREMENT NOT NULL,
#   name TEXT NOT NULL,
#   url_image TEXT NOT NULL,
#   description TEXT,
#   price TEXT NOT NULL,
#   extras TEXT,
#   id_restaurants INTEGER NOT NULL,
#   CONSTRAINT PK_products PRIMARY KEY (id)








#  def post(self):
#         RestaurantModel.setConnectDataBase(db)
#         SerieModel.setConnectDataBase(db)

#         parser = reqparse.RequestParser()
#         parser.add_argument(
#             "id_serie", type=int, required=True, help="Serie cannot be blank"
#         )
#         parser.add_argument(
#             "title", type=str, required=True, help="Title cannot be blank"
#         )
#         parser.add_argument(
#             "resume", type=str, required=True, help="Resume cannot be blank"
#         )
#         parser.add_argument(
#             "season", type=int, required=True, help="Season cannot be blank"
#         )
#         parser.add_argument(
#             "episode_number",
#             type=int,
#             required=True,
#             help="Episode number cannot be blank",
#         )
#         data = parser.parse_args()