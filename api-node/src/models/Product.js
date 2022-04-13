const { Model, DataTypes } = require('sequelize');

class Product extends Model {

  static get _name() {
    return 'Products';
  }

  static init(sequelize) { //recebe a conexão do banco de dados
    return super.init({
      name: {
        type: DataTypes.STRING,
        allowNull: false,
      },
      url_image: {
        type: DataTypes.TEXT,
        allowNull: false,
      },
      description: {
        type: DataTypes.STRING,
        allowNull: false,
      },
      price: {
        type: DataTypes.FLOAT,
        allowNull: false,
      },
      extras: {
        type: DataTypes.TEXT,
        allowNull: false,
      }
    }, {
      hooks: {},
      sequelize,
      defaultScope: {},
    });
  }

  static associate(models) {
  }

}

module.exports = Product;
