from dataclasses import field
from src.util.list import UtilList


class ModelBase:
    __tablename__ = None
    __columns__ = ()
    _db = None

    def __repr__(self) -> str:
        aux = []
        for column in self.__columns__:
            aux.append(f"{column}={self.__dict__[column]}")

        filds = ", \r\n\t".join(aux)
        txt = f"{self.__class__} (\r\n\t{filds}\r\n)"

        return txt

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def to_dict(self):
        values = {}
        for column in self.__columns__:
            values[column] = self.__dict__[column]

        return values

    def insert(self):
        values = {}
        for column in self.__columns__:
            values[column] = self.__dict__[column]

        res = self._db.insert(self.__tablename__, values)
        return res

    def update(self):
        values = {}
        for column in self.__columns__:
            values[column] = self.__dict__[column]
        del values["id"]

        res = self._db.update(self.__tablename__, values, "id=?", [self.id])
        return res

    def delete(self):
        res = self._db.delete(self.__tablename__, "id=?", [self.id])
        return res

    @classmethod
    def setConnectDataBase(cls, value):
        cls._db = value

    @classmethod
    def find_all(cls, order=""):

        # --
        sql = f"SELECT * FROM {cls.__tablename__}"

        if order:
            sql_order_by = cls.build_order_by(order)
            if sql_order_by:
                sql += f" {sql_order_by}"

        res = cls._db.pquey(sql).fetchall()
        return res

    @classmethod
    def find_by_id(cls, id):
        sql = f"SELECT * FROM {cls.__tablename__} WHERE id = ? "
        res = cls._db.pquey(sql, [id]).fetchone()

        return res

    @classmethod
    def find_by_id_build(cls, id):
        data = cls.find_by_id(id)

        if not data:
            return False

        obj = cls()
        for column in cls.__columns__:
            setattr(obj, column, data[column])

        return obj

    # order = "name-asc,description-desc"
    @classmethod
    def build_order_by(cls, order: str):
        sql = ""
        if order:
            args = order.split(",")
            if args:
                cmds = []
                sql += "ORDER BY "
                for arg in args:
                    col = arg.split("-")
                    fieldOrde = col[0]
                    typeOrder = UtilList.getValue(col, 1, "")

                    aux = f"{fieldOrde}"
                    if typeOrder:
                        aux += f" {typeOrder}"
                    cmds.append(aux)
                sql += ", ".join(cmds)
        return sql
