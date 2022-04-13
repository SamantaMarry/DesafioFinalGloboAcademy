const path = require('path');

require('dotenv').config({
  path: path.resolve(
    __dirname,
    '../',
    `.env.${process.env.NODE_ENV}`,
  ),
});

const app = require('./app');

app.listen(process.env.PORT || '3333');
