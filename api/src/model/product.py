from src.model.model_base import ModelBase


class ProductModel(ModelBase):
    __tablename__ = "products"
    __columns__ = ("id", "name", "url_image", "description", "price", "extras", "id_restaurant")

    id = None


    def build(self, name, url_image, description, price, extras, id_restaurant, id=None):
        self.id = id
        self.name = name
        self.url_image = url_image
        self.description = description
        self.price = price
        self.extras = extras
        self.id_restaurant = id_restaurant
        return self