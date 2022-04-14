import { PageMainSite } from "../../../components/PageMainSite"
import { CardContent } from "../../../components/CardContent"
import { useEffect, useState } from "react";
import api from "../../../services/api";

import './style.css'
import Button from './../../../components/Button/Button';

export default function Restaurant() {
  const [restaurants, setRestaurants] = useState({
    name: "",
    address: "",
    description: "",
    url_image: "",
    responsible_name: "",
  });
  const [message, setMessage] = useState({});

  useEffect(() => {
    console.log("🚀 ~ file: Cadastro.jsx ~ line 28 ~ api.post ~ restaurants", restaurants)

  
  }, [])

  const save = (ev) => {
    ev.preventDefault();
    api.post('/restaurants', restaurants).then(response => {
      setMessage({type: 'sucess', message: "Restaurante cadastrado com sucesso!"});
    });
      
  }

  const changeField = (ev) => {
    const newRestaurant = { ...restaurants };
    const { name, value } = ev.currentTarget;
    newRestaurant[name] = value;
    setRestaurants(newRestaurant);
  }

  return (
    <>
      <PageMainSite useFooter={false}>
        {message.message && message.message.trim().length > 0 && (
          <div
            className={`alert-${message.type}`}
            role="alert"
          >
            {message.message}
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
        <div className="c-admin-page-restaurant-cadastro">
          <CardContent title="Restaurante">
            <div className="c-card-content_left">
              <input
                value={restaurants.name}
                onChange={changeField}
                type="text"
                name="name"
              />
              <textarea 
              value={restaurants.description} 
              onChange={changeField} 
              name="description" 
              rows="5" cols="30"></textarea>
            </div>
            <div className="c-card-content_right">
              <input
                value={restaurants.address}
                onChange={changeField}
                type="text"
                name="address"
              />
              <input
                value={restaurants.url_image}
                onChange={changeField}
                type="text"
                name="url_image"
              />
              <input
                value={restaurants.responsible_name}
                onChange={changeField}
                type="text"
                name="responsible_name"
              />
                <Button
                title="Salvar"
                type="submit"
                onClick={(e) => save(e)}
              ></Button>
            </div>
          </CardContent>
        </div>
      </PageMainSite>
    </>
  );
}