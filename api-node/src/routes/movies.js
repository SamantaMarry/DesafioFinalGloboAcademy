const express = require('express');
const routes = express.Router();

const MoviesController = require('@/src/controllers/MoviesController');

routes.get('/', MoviesController.index);
routes.get('/:id', MoviesController.get);
routes.post('/', MoviesController.create);

module.exports = routes;
