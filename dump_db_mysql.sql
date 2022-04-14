
CREATE TABLE IF NOT EXISTS restaurants (
  id INTEGER AUTO_INCREMENT NOT NULL,
  name VARCHAR(100) NOT NULL,
  address VARCHAR(255) NOT NULL,
  description VARCHAR(255) NULL,
  url_image TEXT NOT NULL,
  responsible_name VARCHAR(100) NOT NULL,
  CONSTRAINT PK_restaurants PRIMARY KEY (id)
);

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

-- RESTAURANTS
INSERT INTO jsonsfood.restaurants (name, address, description, url_image, responsible_name) VALUES('Bevin Valentim', '44710 Springs Point', 'French', 'https://www.collinsdictionary.com/images/full/restaurant_135621509.jpg', 'Amandie Ramble');
-- PRODUCTS
INSERT INTO jsonsfood.products (name, url_image, description, price, extras, id_restaurant) VALUES('Sushi', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRye8VP9JUUyyfMha0Yl7VHcH4ouPCyZNH6g&usqp=CAU', 'Japanese Food', 8.17, 'Syrup - Monin - Granny Smith', 1);