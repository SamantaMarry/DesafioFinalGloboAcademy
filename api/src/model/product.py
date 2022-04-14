from src.model.model_base import ModelBase


class ProductModel(ModelBase):
    __tablename__ = "products"
    __columns__ = (
        "id",
        "name",
        "url_image",
        "description",
        "price",
        "extras",
        "id_restaurant",
    )

    id = None

    def build(
        self, name, url_image, description, price, extras, id_restaurant, id=None
    ):
        self.id = id
        self.name = name
        self.url_image = url_image
        self.description = description
        self.price = price
        self.extras = extras
        self.id_restaurant = id_restaurant
        return self

    @classmethod
    def find_all_prodcts_restaurant_id(cls, id, order=""):

        # --
        sql = f"SELECT * FROM {cls.__tablename__} WHERE id_restaurant = %s "

        if order:
            sql_order_by = cls.build_order_by(order)
            if sql_order_by:
                sql += f" {sql_order_by}"

        print(sql)

        res = cls._db.pquey(sql, [id]).fetchall()
        return res
