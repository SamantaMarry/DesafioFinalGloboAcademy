const { Model, DataTypes } = require('sequelize');

class Product extends Model {

  static get _name() {
    return 'Products';
  }

  static init(sequelize) {
    return super.init({
      name: {
        type: DataTypes.STRING,
        allowNull: false,
        validate: {
          notEmpty: true,
          is: /^[A-Za-z\s]+$/i
        }
      },
      url_image: {
        type: DataTypes.TEXT,
        allowNull: false,
      },
      description: {
        type: DataTypes.STRING,
        allowNull: false,
        defaultValue: ""
      },
      price: {
        type: DataTypes.FLOAT,
        allowNull: false,
      },
      extras: {
        type: DataTypes.TEXT,
        allowNull: false,
        defaultValue: ""
      }
    }, {
      tableName: 'products',
      hooks: {},
      sequelize,
      defaultScope: {},
    });
  }

  static associate(models) {
    this.belongsTo(models.Restaurant, { foreignKey: 'id_restaurant', as: 'restaurant' });
  }

}

module.exports = Product;
