const express = require('express');
const router = express.Router();
const ProductModel = require('#src/models/Product');
const RestaurantModel = require('#src/models/Restaurant');

module.exports = {

  routes() {
    // router.post('/', this.create);
    router.get('/:id', this.get);
    router.put('/:id', this.update);
    router.delete('/:id', this.delete);
    return router;
  },

  async get(req, res) {
    try {
      const { id } = req.params;
      const result = await ProductModel.findByPk(id);

      if (!result) {
        return res.status(404).json({ error: 'Product not found' });
      }

      return res.json({ data: result });

    } catch (e) {
      return res.status(400).json({ error: e });
    }
  },

  async update(req, res) {
    const t = await ProductModel.sequelize.transaction();

    try {
      const { id } = req.params;
      let product = await ProductModel.findByPk(id);
      if (!product) return res.status(404).json({ error: 'Product not found' });

      const { ...bodyUser } = req.body;

      let restaurant = await RestaurantModel.findByPk(bodyUser.id_restaurant);
      if (!restaurant) return res.status(404).json({ error: 'Restaurant not found' });

      product = await product.update(bodyUser, t);
      await t.commit();

      return res.set('Location', `${process.env.BASE_URL_API}/products/${product.id}`).send();

    } catch (e) {
      await t.rollback();
      return res.status(400).json({ error: e });
    }
  },

  async delete(req, res) {
    const t = await ProductModel.sequelize.transaction();

    try {
      const { id } = req.params;
      const product = await ProductModel.findByPk(id);

      if (!product) {
        return res.status(400).json({ error: 'Product not found' });
      }
      const result = await product.destroy({ transaction: t });
      await t.commit();

      return res.json({ data: result });

    } catch (e) {
      await t.rollback();
      return res.status(400).json({ error: e });
    }
  },

  // async create(req, res) {
  //   const t = await ProductModel.sequelize.transaction();

  //   try {
  //     const { ...data } = req.body;
  //     const product = await ProductModel.create(data, { transaction: t });
  //     await t.commit();

  //     //return res.json({ data: product });
  //     return res.set('Location', `${process.env.BASE_URL_API}/products/${product.id}`).send();

  //   } catch (e) {
  //     return res.status(400).json({ error: e });
  //   }

  // },

};
