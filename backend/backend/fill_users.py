from backend.models import *
import numpy as np
import random
import names

num_users = 100

for j in range(num_users):
    phonenumber = '99' + ''.join(random.choice("0123456789") for _ in range(6))
    username = names.get_first_name()
    print(phonenumber, username)
    user = User(Userlatitude=np.random.normal(35.15938300, 0.1), Userlongitude=np.random.normal(33.39632500, 0.1), Userphonenumber=phonenumber, UserName=username)
    user.save()