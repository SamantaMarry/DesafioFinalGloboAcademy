const RestaurantModel = require('@/src/models/Restaurant');

module.exports = {

  async index(req, res) {

    try {
      const { rows, count } = await RestaurantModel.findAndCountAll();
      return res.json({ data: { rows, count } });

    } catch (e) {
      return res.status(400).json({ error: e });
    }

  },

  async get(req, res) {
    try {
      const { id } = req.params;
      const result = await RestaurantModel.findByPk(id);

      if (!result) {
        return res.status(400).json({ error: 'Restaurant not found' });
      }

      return res.json({ data: result });

    } catch (e) {
      return res.status(400).json({ error: e });
    }
  },

  async create(req, res) {
    const t = await RestaurantModel.sequelize.transaction();

    try {
      const { ...data } = req.body;
      const restaurant = await RestaurantModel.create(data, { transaction: t });
      await t.commit();

      return res.json({ data: restaurant });

    } catch (e) {
      return res.status(400).json({ error: e });
    }

  }

};
