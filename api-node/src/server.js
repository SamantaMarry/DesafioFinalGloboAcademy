const path = require('path');

if (process.env.NODE_ENV != 'prod') {
  require('dotenv').config({
    path: path.resolve(
      __dirname,
      '../',
      `.env.${process.env.NODE_ENV}`,
    ),
  });
} else {
  require('dotenv').config()
}

const app = require('./app');

app.listen(process.env.PORT || '3333', '0.0.0.0');
