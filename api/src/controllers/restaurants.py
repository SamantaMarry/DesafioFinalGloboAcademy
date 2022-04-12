from flask_restful import Resource, reqparse
from src.model.restaurant import RestaurantModel
from src.server.instance import server
from src.server.db import db

api = server.api

class RestaurantController(Resource):
    @classmethod
    def routes(self):
        api.add_resource(Restaurant, "/restaurants/<int:id>")
        api.add_resource(RestaurantList, "/restaurants")
 
class Restaurant(Resource):
    def get(self, id):
        print('Restaurant GET \o/ {}'.format(id))

    def put(self, id):
        print('Restaurant PUT \o/ {}'.format(id))

    def delete(self, id):
        print('Restaurant DELETE \o/ {}'.format(id))
 
class RestaurantList(Resource):

    def get(self):
        print('RestaurantList GET \o/')
        RestaurantModel.setConnectDataBase(db)
        # commita ai XD
        try:
            restaurants = RestaurantModel.find_all()
            print('-------------------')
            print(restaurants)
        except Exception as error:
            return {"Error": str(error)}, 400
        return restaurants

    def post(self):
        RestaurantModel.setConnectDataBase(db)

        parser = reqparse.RequestParser()
        parser.add_argument(
            "name", type=str, required=True, help="Name cannot be blank"
        )
        parser.add_argument(
             "address", type=str, required=True, help="Address cannot be blank"
        )
        parser.add_argument(
            "description", type=str, required=False 
        )
        parser.add_argument(
            "url_image", type=str, required=True, help="url_image cannot be blank"
        )
        parser.add_argument(
            "responsible_name", type=str, required=True, help="responsible_name cannot be blank"
        )
        data = parser.parse_args()

        restaurant = RestaurantModel().build(
            data.name, data.address, data.description, data.url_image, data.responsible_name
        )
        try:
            lastid = restaurant.insert().lastrowid
        except Exception as error:
            return {"Error": str(error)}, 400
        
        return None, 201, {"Location": f"http://127.0.0.1:5000/restaurants/{lastid}"}

