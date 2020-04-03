from backend.models import *
import numpy as np
import random
import names

# Adds a pastorder for each user
users = User.objects.all()
for user in users:
    if len(PastOrder.objects.filter(UserID=user.UserID, OrderDelivered=False))>0:
        continue
    shop = random.choice(Shop.objects.all())
    available_items = Price.objects.all().filter(ShopID=shop.ShopID)
    num_of_items = 0
    while num_of_items<1 or num_of_items>len(available_items):
        num_of_items = int(np.random.normal(7, 2))

    items = random.sample(list(available_items), num_of_items)
    
    order = PastOrder(UserID=user, OrderDelivered=False)
    order.save()
    for item in items:
        order_item = OrderItems(OrderID=order, PriceID=item, Quantity=random.randint(1, 5))
        order_item.save()
    
