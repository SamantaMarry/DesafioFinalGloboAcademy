"use strict"; // typical JS thing to enforce strict syntax

const fs = require("fs"); // file system for grabbing files
const path = require("path"); // better than '\/..\/' for portability
const Sequelize = require("sequelize"); // Sequelize is a constructor
const basename = path.basename(__filename);
const dirmodels = path.resolve(__dirname, '../models');
const config = require('#src/config/database');

const dbs = {};
const sequelize = new Sequelize(
  config
);

sequelize.authenticate().then(() => {
  console.log('DB connection sucessful');
},
  (err) => {
    console.log(`Error: ${err.message}`);
  });

fs
  .readdirSync(dirmodels)
  .filter(file => {
    return (file.indexOf('.') !== 0) && (file !== basename) && (file.slice(-3) === '.js');
  })
  .forEach(file => {
    let model = require(path.join(dirmodels, file));
    dbs[model.name] = model.init(sequelize);
  });

Object.keys(dbs).forEach(modelName => {
  if (dbs[modelName].associate) {
    dbs[modelName].associate(sequelize.models);
  }
});

dbs.Sequelize = Sequelize;
dbs.sequelize = sequelize;
module.exports = dbs;
