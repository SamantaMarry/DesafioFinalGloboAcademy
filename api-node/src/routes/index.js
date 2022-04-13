const express = require('express');
const routes = express.Router();

const testRoutes = require('./test');

/**
 * ROTAS
 */
// const userRoutes = require('./movies');

/** ==========================================================*/
/** Rotas */
routes.get('/', async (req, res) => res.json({
  sucess: true,
  message: "Hello Word",
  data: null
}));

routes.use('/test', testRoutes);

module.exports = routes;
