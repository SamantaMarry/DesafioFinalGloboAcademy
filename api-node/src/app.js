/** Data Base */
require('#src/database/index');

const express = require('express');
const cors = require('cors');
const routes = require('#src/routes/index');
const app = express();

app.use(cors());
app.use(express.json());
app.use(routes);

module.exports = app;


