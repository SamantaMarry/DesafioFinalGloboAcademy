import { PageMainSite } from "../../../components/PageMainSite";
import { useEffect, useState } from "react";
import api from "../../../services/api";

// import { CardMenu } from "./components/CardMenu"

import "./style.css";
import CardMenu from "./components/CardMenu/CardMenu";

export default function ProductsRestaurant() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    api.get("/products").then((response) => {
      setProducts(response.data);
    });
  }, []);
  return (
    <>
      <PageMainSite>
        <div
          className="c-site-page-products-restaurant"
          style={{ color: "white" }}
        >
          <h1>Produtos</h1>
          <div className="container-card-menu">
            {products.map((item) => (
              <CardMenu className="card-menu"
                key={item.id}
                url_image={item.url_image}
                name={item.name}
                description={item.description}
              />
            ))}
          </div>
        </div>
      </PageMainSite>
    </>
  );
}
