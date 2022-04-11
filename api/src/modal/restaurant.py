from api.src.modal.modal_base import ModelBase


class RestauranteModel(ModelBase):
    __tablename__ = "restaurant"
    __columns__ = ("id", "name", "address", "description", "url_image", "responsible_name")

    id = None


    def build(self, name, address, description, url_image, responsible_name, id=None):
        self.id = id
        self.name = name
        self.address = address
        self.description = description
        self.url_image = url_image
        self.responsible_name = responsible_name
        return self