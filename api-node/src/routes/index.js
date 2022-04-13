const express = require('express');
const routes = express.Router();

const RestaurantController = require('#src/controllers/RestaurantController');
const ProductController = require('#src/controllers/ProductController');

/** ==========================================================*/
/** Rotas */
routes.get('/health', async (req, res) => res.json({
  success: true,
  message: "Hello Word",
  data: null
}));

routes.use('/restaurants', RestaurantController.routes());
routes.use('/products', ProductController.routes());

module.exports = routes;
