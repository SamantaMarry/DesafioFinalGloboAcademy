import { BrowserRouter, Routes, Route } from 'react-router-dom';

import { Home as Home_static } from './pages/site/Home_static'
import { Home } from './pages/site/Home'
import { ProductsRestaurant } from './pages/site/ProductsRestaurant'
import { Restaurants } from './pages/site/Restaurants'

import { ProductCadastro } from './pages/admin/Product'
import { RestaurantCadastro } from './pages/admin/Restaurant'


function Routers() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/h2" element={<Home_static />} />
        <Route path="/products" element={<ProductsRestaurant />} />
        <Route path="/restaurants" element={<Restaurants />} />

        {/* admin */}
        <Route path="/admin/restaurant/cadastro" element={<RestaurantCadastro />} />
        <Route path="/admin/product/cadastro" element={<ProductCadastro />} />
      </Routes>
    </BrowserRouter>
  );
}

export default Routers;
