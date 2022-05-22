import os
import mysql.connector
from mysql.connector import errorcode


class db_mysql:
    def __init__(self) -> None:
        print("-- init db --")
        try:
            self._db_connection = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USERNAME"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_DATABASE"),
            )

            if self._db_connection.is_connected():
                db_info = self._db_connection.get_server_info()
                print("Conectado ao servidor MYSQL versão ", db_info)
                self._cursor = self._db_connection.cursor(
                    dictionary=True, buffered=True
                )

        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database doesn't exist")
            elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("User name or password is wrong")
            else:
                print(error)

    def __del__(self) -> None:
        if self._db_connection.is_connected():
            self._cursor.close()
            self._db_connection.close()
            print("Conexão ao MySQL foi encerrada")

    # --

    def commit(self):
        self._db_connection.commit()

    def pquey(self, sql, args=[]):
        try:
            print("Cursor: {}".format(self._cursor))
            self._cursor.execute(sql, args)
            return self._cursor
        except mysql.connector.Error as err:
            print("Erro SQL: {}".format(err))
            print("SQL: {}".format(sql))
            print("Args: {}".format(args))
            exit(1)

    def pquey_commit(self, sql, args=[]):
        res = self.pquey(sql, args)
        self._db_connection.commit()
        return res

    def insert(self, table, values):
        fields = []
        parms_bind = []
        args = []
        for field, value in values.items():
            fields.append(field)
            parms_bind.append("%s")
            args.append(value)

        # ','.join(str(v) for v in fields)
        fields_insert = ", ".join(fields)
        binds_insert = ", ".join(parms_bind)

        sql = f"""
            INSERT INTO {table} ({fields_insert})
            VALUES ({binds_insert})
        """
        res = self.pquey_commit(sql, args)

        return res

    def update(self, table, values, where, args=[]):
        fields = []
        args_values = []
        for field, value in values.items():
            fields.append(f"{field} = %s")
            args_values.append(value)

        fields_insert = ", ".join(fields)
        args = args_values + args

        sql = f"""
            UPDATE {table} SET {fields_insert}
            WHERE 1=1 AND {where}
        """

        res = self.pquey_commit(sql, args)
        return res

    def delete(self, table, where, args=[]):
        sql = f"""
            DELETE FROM {table}
            WHERE 1=1 AND {where}
        """
        res = self.pquey_commit(sql, args)

        return res

    def sql_create_db(self):
        sqls = [
            """
            CREATE TABLE IF NOT EXISTS restaurants (
              id INTEGER AUTO_INCREMENT NOT NULL,
              name VARCHAR(100) NOT NULL,
              address VARCHAR(255) NOT NULL,
              description VARCHAR(255) NULL,
              url_image TEXT NOT NULL,
              responsible_name VARCHAR(100) NOT NULL,
              CONSTRAINT PK_restaurants PRIMARY KEY (id)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS products (
              id INTEGER AUTO_INCREMENT NOT NULL,
              name VARCHAR(255) NOT NULL,
              url_image TEXT NOT NULL,
              description VARCHAR(255) NULL,
              price FLOAT NOT NULL,
              extras TEXT NULL,
              id_restaurant INTEGER NOT NULL,
              CONSTRAINT PK_products PRIMARY KEY (id),
              CONSTRAINT FK_products_restaurants FOREIGN KEY (id_restaurant) REFERENCES restaurants (id)
            );
          """,
            """INSERT INTO jsonsfood.restaurants (name, address, description, url_image, responsible_name) VALUES('Bevin Valentim', '44710 Springs Point', 'French', 'https://www.collinsdictionary.com/images/full/restaurant_135621509.jpg', 'Amandie Ramble');""",
            """INSERT INTO jsonsfood.restaurants (name, address, description, url_image, responsible_name) VALUES('Beau Lofts', '57847 Maywood Trail', 'Italian', 'https://media-cdn.tripadvisor.com/media/photo-s/13/a2/cc/04/amore-s-italian-restaurant.jpg', 'Delano Campbell');""",
            """INSERT INTO jsonsfood.restaurants (name, address, description, url_image, responsible_name) VALUES('Martica Ashingden', '6004 Dexter Alley', 'Mexican', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCr0bvXRKKet3oHEedvaR6xyn8fQreOtKf8A&usqp=CAU', 'Milzie Ollerhead');""",
            """INSERT INTO jsonsfood.restaurants (name, address, description, url_image, responsible_name) VALUES('Maxy Allom', '92877 Dakota Terrace', 'Fast food', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCr0bvXRKKet3oHEedvaR6xyn8fQreOtKf8A&usqp=CAU', 'Saunderson Neissen');""",
            """INSERT INTO jsonsfood.restaurants (name, address, description, url_image, responsible_name) VALUES('Ealasaid Setterthwait', '69606 Paget Park', 'Italian', 'https://cf.bstatic.com/data/xphoto/1182x887/222/22281452.jpg?size=S', 'Alano Klampk');""",
            """INSERT INTO jsonsfood.restaurants (name, address, description, url_image, responsible_name) VALUES('Elle Karmel', '57936 Ryan Court', 'Japanese', 'https://anaclaudiathorpe.ne10.uol.com.br/wp-content/uploads/2021/05/F50A0085-7C08-4357-91E8-F81E5A7CCCA7.jpeg', 'Justen Swalough');""",
            """INSERT INTO jsonsfood.restaurants (name, address, description, url_image, responsible_name) VALUES('Rachele Wynn', '5997 Blue Bill Park Road', 'Street Food', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTbLnIvX_FA7C6XqHkQKRfKl6JxLCUMa-rJqw&usqp=CAU', 'Duncan Brogiotti');""",
            """INSERT INTO jsonsfood.restaurants (name, address, description, url_image, responsible_name) VALUES('Jeremiah Gierck', '9 Monterey Junction', 'Brazilian', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSCLxhQ7SXE9DscoWxgs7oM0SLLVzPCPdb2g&usqp=CAU', 'Carmine Shutle');""",
            """INSERT INTO jsonsfood.restaurants (name, address, description, url_image, responsible_name) VALUES('Gertrude Scherer', '69 Crownhardt Terrace', 'Japanese', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzP40Iwi8cdE6zDM3rtRit3VJqDQCajyGecw&usqp=CAU', 'Morris Wheaton');""",
            """INSERT INTO jsonsfood.restaurants (name, address, description, url_image, responsible_name) VALUES('Courtney Winterflood', '4069 Brown Hill', 'French', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHTwxxtgW2W84s--p5NDlHrdaL4ZdEo_aP-A&usqp=CAU', 'Remington Dunklee');""",
            """INSERT INTO jsonsfood.restaurants (name, address, description, url_image, responsible_name) VALUES('Moina Luquet', '5037 Pearson Crossing', 'Japanese', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQTwP8ImneAyqJOqtA1DZS5EofWaxgeQYcs6VJnKFzRzeeTl9gzmxsbbPJ5sM8BP_1LcmQ&usqp=CAU', 'Perice Yerborn');""",
            """INSERT INTO jsonsfood.restaurants (name, address, description, url_image, responsible_name) VALUES('Dorri Flaonier', '49 Tony Way', 'Fast Food', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQ27r1cRy8ivMOYdxvDbmCGhPLx-brAiuwmdQUxNGVx8RfVDT43smK9ICuFOSH7aY022g&usqp=CAU', 'Cathryn Purrier');""",
            """INSERT INTO jsonsfood.restaurants (name, address, description, url_image, responsible_name) VALUES('Tully Rittelmeyer', '1 Swallow Terrace', 'Indian', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ8EZsFAsDjNrXxIGRaeB2ww73LUPB8Of4GWgoNs3Q8la1HQgKE_HI36CQFLwQWih-F5BA&usqp=CAU', 'Jacquie Kinsey');""",
            """INSERT INTO jsonsfood.restaurants (name, address, description, url_image, responsible_name) VALUES('Miller Gradly', '977 Carey Way', 'Italian', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQAfWwZBJVVuFpgPpXfnPKmstFd_ZVRJV1H-I7j1WraE330Et1hTCGIYOVRCwZfJMQNy0Q&usqp=CAU', 'Norris Tilt');""",
            """INSERT INTO jsonsfood.restaurants (name, address, description, url_image, responsible_name) VALUES('Debor Renfree', '59643 Ramsey Trail', 'French', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT196odUf3WpjgHkBOQjM9EzB5u6HOL_cVceohhb0KfY84U-QgSSHVenxuzqlfnUywJfkI&usqp=CAU', 'Omero Dubarry');""",
            """INSERT INTO jsonsfood.products (name, url_image, description, price, extras, id_restaurant) VALUES('Sushi', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRye8VP9JUUyyfMha0Yl7VHcH4ouPCyZNH6g&usqp=CAU', 'Japanese Food', 8.17, 'Syrup - Monin - Granny Smith', 1);""",
            """INSERT INTO jsonsfood.products (name, url_image, description, price, extras, id_restaurant) VALUES('Pizza', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSeTYGOTjXZzHs26qMEfnmw6qe3MNiG-KSKsbh4I8lz8OgRjl7yDWs83ohdjhzQpyki0bc&usqp=CAU', 'Napolitan Pizza', 13.65, 'Pectin', 1);""",
            """INSERT INTO jsonsfood.products (name, url_image, description, price, extras, id_restaurant) VALUES('Croassaint', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTd55JcaxnfjlHrhWzvcgSqSpE2VX0tRzGnbaGO9FY_yy5HsRS8H4Q_9yTCakbpKMXsHBU&usqp=CAU', 'French Bakeries', 14.23, 'Flour - All Purpose', 1);""",
            """INSERT INTO jsonsfood.products (name, url_image, description, price, extras, id_restaurant) VALUES('Churrasco', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSK5y3xcyOFdMVt7qvcwWW2ZRf30Et6RtcX4g&usqp=CAU', 'Brazilian Food', 17.84, 'Beef - Rouladin, Sliced', 1);""",
            """INSERT INTO jsonsfood.products (name, url_image, description, price, extras, id_restaurant) VALUES('Tuer', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOImM1PsvnLCY8RpLYC_XMrfbty6eNuF-uAg&usqp=CAU', 'Indian Food', 22.28, 'Sping Loaded Cup Dispenser', 2);""",
            """INSERT INTO jsonsfood.products (name, url_image, description, price, extras, id_restaurant) VALUES('Soup', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRMNs2g8v99sOI-G_vjI4wssJvKiGjyW83FhK1dzcC519rrp0zhM2U5gWqxgWZGG79jhRk&usqp=CAU', 'French food', 7.75, 'Pork - Tenderloin, Fresh', 3);""",
            """INSERT INTO jsonsfood.products (name, url_image, description, price, extras, id_restaurant) VALUES('Sashimi', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHCzb8_510HSbVUZgXJU6m4EHt0UXFH4OugA&usqp=CAU', 'Japanese Food', 8.33, 'Cup - 6oz, Foam', 4);""",
        ]

        try:
            for slq in sqls:
                self._cursor.execute(slq)
            self._db_connection.commit()
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database doesn't exist")
            elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("User name or password is wrong")
            else:
                print(error)
