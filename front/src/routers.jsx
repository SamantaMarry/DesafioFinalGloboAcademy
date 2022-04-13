import { BrowserRouter, Routes, Route } from 'react-router-dom';

import { Home } from './pages/Home'

import { Home as Home2 } from './pages/site/Home2'
import { ProductsRestaurant } from './pages/site/ProductsRestaurant'
import { Restaurants } from './pages/site/Restaurants'

import { ProductCadastro } from './pages/admin/Product'
import { RestaurantCadastro } from './pages/admin/Restaurant'


function Routers() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/h2" element={<Home2 />} />
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
