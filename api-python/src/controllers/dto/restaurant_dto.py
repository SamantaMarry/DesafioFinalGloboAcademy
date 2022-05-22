from flask_restful import reqparse
from marshmallow import Schema, fields

# https://pythonacademy.com.br/blog/domine-decorators-em-python


class RestaurantDtoMarshmallow(Schema):
    """
    Way of use:

    try:
        restaurant_schema = RestaurantDtoMarshmallow()
        req = restaurant_schema.load(request.get_json())
    except ValidationError as err:
        return err.messages, 422

    print(req)
    """

    name = fields.Str(
        required=True, error_messages={"required": "Name cannot be blank"}
    )
    address = fields.Str(
        required=True, error_messages={"required": "address cannot be blank"}
    )
    description = fields.Str(required=False)
    url_image = fields.Str(
        required=True, error_messages={"required": "url_image cannot be blank"}
    )
    responsible_name = fields.Str(
        required=True, error_messages={"required": "responsible_name cannot be blank"}
    )


class RestaurantDtoRestfull:
    """
    Way of use:

    data = RestaurantDtoRestfull().getArgs()
    print(data)
    """

    def __init__(self) -> None:
        parser = reqparse.RequestParser()
        parser.add_argument(
            "name",
            type=str,
            required=True,
            help="Name cannot be blank",
            location="form",
        )
        parser.add_argument(
            "address",
            type=str,
            required=True,
            help="Address cannot be blank",
            location="form",
        )
        parser.add_argument("description", type=str, required=False)
        parser.add_argument(
            "url_image",
            type=str,
            required=True,
            help="url_image cannot be blank",
            location="form",
        )
        parser.add_argument(
            "responsible_name",
            type=str,
            required=True,
            help="responsible_name cannot be blank",
            location="form",
        )

        self.data = parser.parse_args()

    def getArgs(self):
        return self.data
