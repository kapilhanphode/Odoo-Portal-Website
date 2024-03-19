from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from datetime import datetime


class Products111(models.Model):
    _name = "products"
    _rec_name = 'product_id'

    product_id = fields.Integer('Product id')
    product_name = fields.Char('Product Name')
    product_description = fields.Char('Product Description')
    product_category = fields.Char('Product Category')
    veg_non_veg = fields.Selection([('veg', 'Veg'), ('nveg', 'Non-Veg')], 'Product Type')
    product_rating = fields.Float('Product Average Rating', compute='_compute_product_rating', searchable=True)
    ratings_ids = fields.One2many('ratings', 'product_id', 'Ratings')

    @api.depends('ratings_ids.rating_value')
    def _compute_product_rating(self):
        for product in self:
            ratings = product.ratings_ids.filtered(lambda r: r.rating_value is not None)
            if ratings:
                product.product_rating = sum(ratings.mapped('rating_value')) / len(ratings)
            else:
                product.product_rating = 0.0


class ProductToppings(models.Model):
    _name = 'product_toppings'
    _rec_name = 'topping_id'

    product_id = fields.Many2one('products')
    topping_id = fields.Integer('Topping ID')


class Ratings111(models.Model):
    _name = 'ratings'
    _rec_name = 'rating_id'

    rating_id = fields.Integer('Rating ID')
    product_id = fields.Many2one('products', 'Product ID')
    rating_value = fields.Float('Rating Value')
    product_description = fields.Char('Product Description', related='product_id.product_description')


class Toppings(models.Model):
    _name = 'toppings'
    _rec_name = 'topping_id'

    topping_id = fields.Integer('Topping ID')
    group_id = fields.Many2one('toppings_groups', 'Group ID')
    topping_name = fields.Char('Topping Name')


class ToppingsGroups(models.Model):
    _name = 'toppings_groups'
    _rec_name = 'group_id'

    group_id = fields.Integer('Group ID')
    group_name = fields.Char('Group Name')
