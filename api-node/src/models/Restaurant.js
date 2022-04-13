const { Model, DataTypes } = require('sequelize');

class Restaurant extends Model {

  static get _name() {
    return 'Restaurants';
  }

  static init(sequelize) {
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
        defaultValue: ""
      },
      url_image: {
        type: DataTypes.TEXT,
        allowNull: false,
        validate: {
          notEmpty: true,
        }
      },
      responsible_name: {
        type: DataTypes.STRING,
        allowNull: false,
        validate: {
          notEmpty: true,
          is: /^[A-Za-z\s]+$/i
        }
      }
    }, {
      tableName: 'restaurants',
      hooks: {},
      sequelize,
      defaultScope: {},
    });
  }

  static associate(models) {
    this.hasOne(models.Product, { foreignKey: 'id_restaurant', as: 'product' });
  }

}

module.exports = Restaurant;
