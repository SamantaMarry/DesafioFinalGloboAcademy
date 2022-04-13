import { PageMainSite } from "../../../components/PageMainSite"
import { CardContent } from "../../../components/CardContent"
import { useEffect, useState } from "react";
import api from "../../../services/api";

import './style.css'
import Button from './../../../components/Button/Button';

export default function Restaurant() {
  const [restaurants, setRestaurants] = useState({
    id: 0,
    name: "",
    address: "",
    description: "",
    url_image: "",
    responsible_name: "",
  });
  const [loading, setLoading] = useState(false);

  const save = (ev) => {
    ev.preventDefault();
    setLoading(true);
    api.post("/restaurants", restaurants)
      .then(response => {
        setLoading(false);
        console.log(response);
      })
      .catch(error => {
        setLoading(false);
        console.log(error);
      });
  }
  
  

  const changeFild = (ev) => {
    const newRestaurant = { ...restaurants };
    const { name, value } = ev.currentTarget;
    newRestaurant[name] = value;
    setRestaurants(newRestaurant);
  }


  return (
    <>
      <PageMainSite useFooter={false}>
        <div className="c-admin-page-restaurant-cadastro">
          <CardContent title="Restaurante">
            <div className="c-card-content_left">
              <input value = {restaurants.name}onChange={changeFild}type="text" name='name' />
              <textarea name="description" rows="5" cols="30"></textarea>
            </div>
            <div className="c-card-content_right">

              <input value = {restaurants.address} onChange={changeFild} type="text" name='address' />
              <input value = {restaurants.url_image}onChange={changeFild} type="text" name='url_image' />
              <input value = {restaurants.responsible_name}onChange={changeFild} type="text" name='responsible_name' />
              <Button title="Salvar" onClick={save}>Salvar</Button>
            </div>
          </CardContent>
        </div>
      </PageMainSite>
    </>
  )
}