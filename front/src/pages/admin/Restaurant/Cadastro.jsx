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

  /*
  useEffect(() => {
    //console.log("🚀 ~ file: Cadastro.jsx ~ line 28 ~ api.post ~ restaurants", restaurants)
  }, [])*/

  const save = (ev) => {
    ev.preventDefault();
    api.post('/restaurants', restaurants).then(response => {
      setMessage({ type: 'sucess', message: "Restaurante cadastrado com sucesso!" });
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
            className={`alert alert-${message.type}`}
            role="alert"
          >
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
        <div className="c-admin-page-restaurant-cadastro">
          <CardContent title="Restaurante">
            <div className="c-card-content_left">
              <label htmlFor="">Nome do restaurante</label>
              <input
                value={restaurants.name}
                onChange={changeField}
                type="text"
                name="name"
                placeholder="Digite o nome do restaurante"
              />
              <label htmlFor="">Descrição</label>
              <textarea
                value={restaurants.description}
                onChange={changeField}
                name="description"
                rows="5" cols="30"
                placeholder="Descrição"
              ></textarea>
            </div>
            <div className="c-card-content_right">
              <label htmlFor="">Endereço</label>
              <input
                value={restaurants.address}
                onChange={changeField}
                type="text"
                name="address"
                placeholder="Digite o endereço"
              />
              <label htmlFor="">Imagem do restaurante</label>
              <input
                value={restaurants.url_image}
                onChange={changeField}
                type="text"
                name="url_image"
                placeholder="Cole a URL da imagem aqui"
              />
              <label htmlFor="">Nome do responsável</label>
              <input
                value={restaurants.responsible_name}
                onChange={changeField}
                type="text"
                name="responsible_name"
                placeholder="Digite o nome do responsável"
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