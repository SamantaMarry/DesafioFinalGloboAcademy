import { useEffect, useState } from "react";
import api from "../../../services/api";
import './style.css';
import catalog from './catalog.svg';

import { PageMainSite } from "../../../components/PageMainSite"
import { CardRestaurants } from "../Home/components/CardRestaurants"

export default function Home() {

  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    api.get("/restaurants").then((response) => {
      console.log(response.data);
      setRestaurants(response.data);
    });
  }, []);

  return (
    <>
      <PageMainSite>
        <main>
          <article id="main-content">
            <section id="search-box">
              <h2>Escolha o seu <br /> restaurante favorito.</h2>
              <div className="c-restaurants-list">
                {restaurants.map((item) => (
                  <CardRestaurants
                    key={item.id}
                    id={item.id}
                    url_image={item.url_image}
                    name={item.name}
                    description={item.description}
                  />
                ))}
              </div>
            </section>

            <section class="food-style">
              <h4>Comida para todo <br />
                gosto!</h4>
              <img src={catalog} />
            </section>

          </article>
        </main>
      </PageMainSite>
    </>
  )

}