import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Home } from './pages/Home'

import { ProductsRestaurant } from './pages/ProductsRestaurant'
import { Restaurants } from './pages/Restaurants'

import { Product } from './pages/admin/Product'
import { Restaurant } from './pages/admin/Restaurant'


function Routers() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/products" element={<ProductsRestaurant />} />
        <Route path="/restaurants" element={<Restaurants />} />

        {/* admin */}
        <Route path="/admin/restaurant" element={<Restaurant />} />
        <Route path="/admin/product" element={<Product />} />
      </Routes>
    </BrowserRouter>
  );
}

export default Routers;
