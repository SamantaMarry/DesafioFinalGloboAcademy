import { PageMainSite } from "../../../components/PageMainSite";
import { CardContent } from "../../../components/CardContent";
import { useEffect, useState } from "react";
import api from "../../../services/api";

import "./style.css";
import Button from "./../../../components/Button/Button";

export default function Product() {
  const [products, setProducts] = useState({
    name: "",
    url_image: "",
    description: "",
    price: 0.0,
    extras: "",
    id_restaurant: 0,
  });
  const [message, setMessage] = useState({});
  const [restaurants, setRestaurants] = useState([]);
  const [selectedRestaurant, setSelectedRestaurant] = useState();

  useEffect(() => {
    _reloadItens();
  }, []);

  const save = (ev) => {
    ev.preventDefault();
    api.post("/products", products).then((response) => {
      setMessage({
        type: "sucess",
        message: "Produto cadastrado com sucesso!",
      });
    });
  };

  const changeField = (ev) => {
    const newProduct = { ...products };
    const { name, value } = ev.currentTarget;
    newProduct[name] = value;
    setProducts(newProduct);
  };

  const _reloadItens = () => {
    api.get("/restaurants").then((response) => {
      setRestaurants(response.data);
    });
  };

  return (
    <>
      <PageMainSite useFooter={false}>
        {message.message && message.message.trim().length > 0 && (
          <div className={` alert alert-${message.type}`} role="alert">
            <p>{message.message}</p>
            <button
              type="button"
              className="close"
              onClick={(event) => setMessage([])}
              aria-label="Close"
            >
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
        )}
        <div className="c-admin-page-products-cadastro">
          <CardContent title="Produto">
            <div className="c-card-content_left">
              <label htmlFor="">Nome do produto</label>
              <input
                value={products.name}
                onChange={changeField}
                type="text"
                name="name"
                placeholder="Digite o nome do produto"
              />
              <label htmlFor="">Preço</label>
              <input
                value={products.price}
                onChange={changeField}
                type="number"
                name="price"
                placeholder="Digite o preço do produto"
              />
              <label htmlFor="">Descrição</label>
              <textarea
                value={products.description}
                onChange={changeField}
                name="description"
                rows="5"
                cols="30"
                placeholder="Descrição"
              ></textarea>
            </div>
            <div className="c-card-content_right">
              <label htmlFor="">Imagem do produto</label>
              <input
                value={products.url_image}
                onChange={changeField}
                type="text"
                name="url_image"
                placeholder="Cole a URL da imagem aqui"
              />
              <label htmlFor="">Extras</label>
              <input
                value={products.extras}
                onChange={changeField}
                type="text"
                name="extras"
                placeholder="Extras"
              />
              <label htmlFor="">Restaurante</label>
              <select
                className="restaurants"
                name="id_restaurant"
                value={selectedRestaurant}
                onChange={changeField}
              >
                {restaurants.map((restaurant) => (
                  <option key={restaurant.id} value={restaurant.id}>
                    {restaurant.name}
                  </option>
                ))}
              </select>
              <Button type="submit" onClick={(e) => save(e)} title="Salvar">
                Salvar
              </Button>
            </div>
          </CardContent>
        </div>
      </PageMainSite>
    </>
  );
}
