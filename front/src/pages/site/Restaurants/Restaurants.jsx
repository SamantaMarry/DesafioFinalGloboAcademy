import { PageMainSite } from "../../../components/PageMainSite"
import { useEffect, useState } from "react";
import api from "../../../services/api";

import './style.css'

export default function Restaurants() {
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    api.get("/restaurants").then((response) => {
      setRestaurants(response.data);
    });
  }, []);

  return (
    <>
      <PageMainSite>
        <div className="c-site-page-restaurants" style={{ color: 'white' }}>
          <h1>Restaurants</h1>
          <ul className='c-table-list'>
            {restaurants.map((item) => (
              <li key={item.id}>
                <div className="c-table-list-item">
                  <div className="c-table-list-item-image">
                    <img src={item.url_image} alt="SEM IMAGEM" />
                  </div>
                  <div className="c-table-list-item-content">
                    <h1>{item.name}</h1>
                    <p>{item.description}</p>
                  </div>
                </div>
              </li>
            ))}
          </ul>
        </div>
      </PageMainSite>
    </>
  )
}