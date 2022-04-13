const ProductModel = require('@/src/models/Product');

module.exports = {

  async index(req, res) {

    try {
      const { rows, count } = await ProductModel.findAndCountAll();
      return res.json({ data: { rows, count } });

    } catch (e) {
      return res.status(400).json({ error: e });
    }

  },

  async get(req, res) {
    try {
      const { id } = req.params;
      const result = await ProductModel.findByPk(id);

      if (!result) {
        return res.status(400).json({ error: 'Product not found' });
      }

      return res.json({ data: result });

    } catch (e) {
      return res.status(400).json({ error: e });
    }
  },

  async create(req, res) {
    const t = await ProductModel.sequelize.transaction();

    try {
      const { ...data } = req.body;
      const product = await ProductModel.create(data, { transaction: t });
      await t.commit();

      return res.json({ data: product });

    } catch (e) {
      return res.status(400).json({ error: e });
    }

  }

};
