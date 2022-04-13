const { Model, DataTypes } = require('sequelize');

class Restaurant extends Model {

  static get _name() {
    return 'Restaurants';
  }

  static init(sequelize) { //recebe a conexão do banco de dados
    return super.init({
      name: {
        type: DataTypes.STRING,
        allowNull: false,
      },
      address: {
        type: DataTypes.STRING,
        allowNull: false,
      },
      description: {
        type: DataTypes.STRING,
        allowNull: false,
      },
      url_image: {
        type: DataTypes.TEXT,
        allowNull: false,
      },
      responsible_name: {
        type: DataTypes.STRING,
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

module.exports = Restaurant;
