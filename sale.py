# -*- coding: utf-8 -*-
"""
    shop

    :copyright: (c) 2014 by Openlabs Technologies & Consulting (P) LTD.
    :license: BSD, see LICENSE for more details
"""
from trytond.model import ModelSQL, ModelView, fields
from trytond.pyson import Eval, Bool

__all__ = ['Shop', 'ShopPrice']


class Shop(ModelSQL, ModelView):
    "Shop"

    __name__ = 'sale.shop'

    name = fields.Char("Name", required=True)

    type = fields.Selection([
        ('ebay', 'eBay'),
        ('amazon', 'Amazon'),
        ('bestbuy', 'Best-Buy'),
    ], "Type", required=True)

    currency = fields.Many2One(
        "currency.currency", "Currency", required=True, select=True
    )

    allow_tier_pricing = fields.Boolean("Allow Tier Pricing ?")


class ShopPrice(ModelSQL, ModelView):
    "Shop Price"

    __name__ = 'product.product.shop_price'

    shop = fields.Many2One(
        "sale.shop", "Shop", required=True, select=True
    )

    quantity = fields.Integer(
        "Quantity", states={
            'required': Bool(Eval('allow_tier_pricing')),
            'invisible': ~Bool(Eval('allow_tier_pricing')),
        }, depends=['allow_tier_pricing']
    )

    currency = fields.Function(
        fields.Many2One(
            "currency.currency", "Currency", on_change_with=['shop']
        ), 'on_change_with_currency'
    )

    price = fields.Numeric("Price", required=True)

    allow_tier_pricing = fields.Function(
        fields.Boolean("Allow Tier Pricing ?", on_change_with=['shop']),
        'on_change_with_allow_tier_pricing'
    )

    def on_change_with_allow_tier_pricing(self, name=None):
        """
        Returns True if shop allows tier pricing
        """
        if self.shop:
            return self.shop.allow_tier_pricing

    def on_change_with_currency(self, name=None):
        """
        Returns currecny of shop
        """
        if self.shop:
            return self.shop.currency.id
