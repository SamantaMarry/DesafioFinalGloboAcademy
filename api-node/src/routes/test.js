const express = require('express');
const routes = express.Router();

routes.get('/', (req, res) => {
  res.json({ result: 'Sucess API test' });
});

module.exports = routes;
