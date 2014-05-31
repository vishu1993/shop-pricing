# -*- coding: utf-8 -*-
'''
    Initialize Module

    :copyright: (c) 2014 by Openlabs Technologies & Consulting (P) Ltd.
    :license: BSD, see LICENSE for more details

'''
from trytond.pool import Pool

from sale import Shop, ShopPrice


def register():
    Pool.register(
        Shop,
        ShopPrice,
        module='shop_pricing', type_='model',
    )
