from backend.models import *
import numpy as np
import random

probability = 0.8
mean_price = 4
stdev = 1
shops = Shop.objects.filter(ShopTypeID=1)
products = Product.objects.all()
for shop in shops:
    for product in products:
        if product.ProductTypeID.ProductTypeID in [8,9,10,37]:
            print(shop, product)
            if random.random() < probability:
                print('saving')
                price = Price(ShopID=shop, ProductID=product, Price=np.random.normal(mean_price, stdev))
                price.save()