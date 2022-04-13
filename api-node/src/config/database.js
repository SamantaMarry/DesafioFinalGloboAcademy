//const config = process.env.NODE_ENV === 'test' ? configuration.test : configuration.development
const env = process.env.NODE_ENV || "dev"; // use process environment

/**
 * SQL Lite3
 *  development: {
    storage: 'path/to/database.sqlite', //process.env.DB_DIALECT
    dialect: process.env.DB_DIALECT
  },
 */

const config = {
  dev: {
    username: process.env.DB_USERNAME,
    password: process.env.DB_PASSWORD,
    database: process.env.DB_DATABASE,
    host: process.env.DB_HOST,
    dialect: process.env.DB_DIALECT,
    define: {
      timestamps: false, /** faz com q todas as tabelas tenham as colunas created_at, updated_at */
      underscored: true /** faz os nomes das tabelas e campos separador por _ */
    }
  },
  test: {
    username: "root",
    password: null,
    database: "database_test",
    host: "10.5.0.5",
    dialect: "mysql",
  },
  prod: {
    username: "root",
    password: null,
    database: "database_production",
    host: "10.5.0.5",
    dialect: "mysql",
  }
}

module.exports = config[env];
