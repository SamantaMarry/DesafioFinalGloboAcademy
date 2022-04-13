import { CardMenu } from "./components/CardMenu"
import api from "../../services/api"
import './style.css'
import { useEffect, useState } from "react"

export default function ProductsRestaurant() {

const [products, setProducts] = useState([])

useEffect (() => {
  api.get("/products").then(response => {
    setProducts(response.data)
  })
}, [])


  return (
    <>
    {products.map(item => (
      <CardMenu key={item.id} url_image={item.url_image} name={item.name} description={item.description} />
    ))}
    </>
  )
}