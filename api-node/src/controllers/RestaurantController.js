const express = require('express');
const router = express.Router();
const RestaurantModel = require('#src/models/Restaurant');
const PaginationClass = require('#src/class/Pagination');

module.exports = {

  routes() {
    // router.post('/', this.create);
    router.get('/', this.index);
    router.get('/:id', this.get);
    router.put('/:id', this.update);
    router.delete('/:id', this.delete);
    return router;
  },

  async index(req, res) {

    try {

      const page = req.query.page || 1;

      const Pagination = new PaginationClass(RestaurantModel);
      const result = await Pagination.select(page);

      return res.json(result.rows);

    } catch (e) {
      return res.status(400).json({ error: e });
    }

  },

  async get(req, res) {
    try {
      const { id } = req.params;
      const result = await RestaurantModel.findByPk(id);

      if (!result) {
        return res.status(404).json({ error: 'Restaurant not found' });
      }

      return res.json({ data: result });

    } catch (e) {
      return res.status(400).json({ error: e });
    }
  },

  async update(req, res) {
    const t = await RestaurantModel.sequelize.transaction();

    try {
      const { id } = req.params;
      let restaurant = await RestaurantModel.findByPk(id);
      if (!restaurant) return res.status(404).json({ error: 'Restaurant not found' });

      const { ...bodyUser } = req.body;

      restaurant = await restaurant.update(bodyUser, t);
      await t.commit();

      return res.set('Location', `${process.env.BASE_URL_API}/restaurants/${restaurant.id}`).send();

    } catch (e) {
      await t.rollback();
      return res.status(400).json({ error: e });
    }
  },

  async delete(req, res) {
    const t = await RestaurantModel.sequelize.transaction();

    try {
      const { id } = req.params;
      const restaurant = await RestaurantModel.findByPk(id);

      if (!restaurant) {
        return res.status(400).json({ error: 'Restaurant not found' });
      }
      const result = await restaurant.destroy({ transaction: t });
      await t.commit();

      return res.json({ data: result });

    } catch (e) {
      await t.rollback();
      return res.status(400).json({ error: e });
    }
  },

  // async create(req, res) {
  //   const t = await RestaurantModel.sequelize.transaction();

  //   try {
  //     const { ...data } = req.body;
  //     const restaurant = await RestaurantModel.create(data, { transaction: t });
  //     await t.commit();

  //     //return res.json({ data: restaurant });
  //     return res.set('Location', `${process.env.BASE_URL_API}/restaurants/${restaurant.id}`).send();


  //   } catch (e) {
  //     return res.status(400).json({ error: e });
  //   }

  // },

};
