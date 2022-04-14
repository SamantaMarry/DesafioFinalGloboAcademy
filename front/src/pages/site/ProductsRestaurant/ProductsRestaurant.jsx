// import { useSearchParams } from "react-router-dom";
import { PageMainSite } from "../../../components/PageMainSite";
import { useEffect, useState } from "react";
import api from "../../../services/api";

import { useQuery } from '../../../hooks/useQuery'

// import { CardMenu } from "./components/CardMenu"

import { useParams, useLocation, Outlet } from 'react-router-dom';
import CardMenu from "./components/CardMenu/CardMenu";
import "./style.css";

export default function ProductsRestaurant(props) {
  const [products, setProducts] = useState([]);

  const { id_restaurant } = useParams();

  useEffect(() => {
    //restaurants/<int:id_restaurant>/product
    api.get(`restaurants/${id_restaurant}/product`).then((response) => {
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
