from flask_restful import reqparse
from marshmallow import Schema, fields

# https://pythonacademy.com.br/blog/domine-decorators-em-python


class ProductDtoMarshmallow(Schema):
    """
    Way of use:

    try:
        product_schema = ProductDtoMarshmallow()
        req = product_schema.load(request.get_json())
    except ValidationError as err:
        return err.messages, 422

    print(req)
    """

    name = fields.Str(
        required=True, error_messages={"required": "Name cannot be blank"}
    )
    url_image = fields.Str(
        required=True, error_messages={"required": "Url image cannot be blank"}
    )
    description = fields.Str(required=False)
    price = fields.Str(
        required=True, error_messages={"required": "Price cannot be blank"}
    )
    extras = fields.Str(required=False)
    id_restaurant = fields.Str(
        required=True, error_messages={"required": "One restaurant should be informed"}
    )


class ProductDtoRestfull:
    """
    Way of use:

    data = ProductDtoRestfull().getArgs()
    print(data)
    """

    def __init__(self) -> None:
        parser = reqparse.RequestParser()
        parser.add_argument(
            "name",
            type=str,
            required=True,
            help="Name cannot be blank",
            location="json",
        )
        parser.add_argument(
            "url_image",
            type=str,
            required=True,
            help="Url image cannot be blank",
            location="json",
        )
        parser.add_argument("description", type=str, required=False, location="json")
        parser.add_argument(
            "price",
            type=float,
            required=True,
            help="Price cannot be blank",
            location="json",
        )
        parser.add_argument("extras", type=str, required=False, location="json")
        parser.add_argument(
            "id_restaurant",
            type=int,
            required=True,
            help="One restaurant should be informed",
            location="json",
        )

        self.data = parser.parse_args()

    def getArgs(self):
        return self.data
