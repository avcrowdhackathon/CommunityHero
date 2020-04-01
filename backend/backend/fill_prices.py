from backend.models import *
import numpy as np
import random

probability = 0.5
mean_price = 4
stdev = 1
shops = Shop.objects.filter(ShopTypeID='1')
products = Product.objects.all()
for shop in shops:
    for product in products:
        if product.ProductTypeID not in [8,9,10,37]: continue
        if random.random() < probability:
            price = Price(ShopID=shop, ProductID=product, Price=np.random.normal(mean_price, stdev))
            price.save()