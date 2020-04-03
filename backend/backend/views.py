from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from backend.models import *
from backend.serializers import *
from django.db.models import Q
import numpy as np
import random
import names

from math import radians, cos, sin, asin, sqrt 
def distance(lat1, lon1, lat2, lon2): 
	  
	# The math module contains a function named 
	# radians which converts from degrees to radians. 
	lon1 = radians(lon1) 
	lon2 = radians(lon2) 
	lat1 = radians(lat1) 
	lat2 = radians(lat2) 
	   
	# Haversine formula  
	dlon = lon2 - lon1  
	dlat = lat2 - lat1 
	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
  
	c = 2 * asin(sqrt(a))  
	 
	# Radius of earth in kilometers. Use 3956 for miles 
	r = 6371
	   
	# calculate the result 
	return(c * r) 

@api_view(['GET'])
def category_collection(request):
	if request.method == 'GET':
		posts = Category.objects.all()
		serializer = CategorySerializer(posts, many=True)
		return Response(serializer.data)


@api_view(['GET'])
def category_element(request, pk):
	try:
		post = Category.objects.get(CategoryID=pk)
	except Category.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = CategorySerializer(post)
		return Response(serializer.data)


@api_view(['GET'])
def producttype_collection(request):
	if request.method == 'GET':
		posts = ProductType.objects.all()
		serializer = ProductTypeSerializer(posts, many=True)
		return Response(serializer.data)

@api_view(['GET'])
def producttype_name(request, name):
	if request.method == 'GET':
		posts = ProductType.objects.filter(Q(ProductTypeName__icontains=name) | Q(CategoryID__CategoryName__icontains=name))
		serializer = ProductTypeSerializer(posts, many=True)
		return Response(serializer.data)

@api_view(['GET'])
def producttype_element(request, pk):
	try:
		post = ProductType.objects.get(ProductTypeID=pk)
	except ProductType.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = ProductTypeSerializer(post)
		return Response(serializer.data)

@api_view(['GET'])
def product_name(request, name):
	if request.method == 'GET':
		posts = Product.objects.filter(Q(ProductName__icontains=name) | Q(ProductTypeID__ProductTypeName__icontains=name))
		serializer = ProductSerializer(posts, many=True)
		return Response(serializer.data)

@api_view(['GET'])
def product_barcode(request):
	barcode = request.query_params['barcode']
	try:
		post = Product.objects.get(ProductBarcode=barcode)
	except Product.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = ProductSerializer(post)
		return Response(serializer.data)

@api_view(['GET'])
def product_element(request, pk):
	try:
		post = Product.objects.get(ProductID=pk)
	except ProductType.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = ProductSerializer(post)
		return Response(serializer.data)

@api_view(['GET'])
def user_radius(request):
	if request.method == 'GET':
		lat = float(request.query_params['lat'])
		lng = float(request.query_params['lng'])
		rad = float(request.query_params['rad'])
		# TODO: Implement direct distance from DB
		users = PastOrder.objects.filter(OrderDelivered=False)
		result_users = []
		for user in users:
			if distance(lat, lng, user.UserID.Userlatitude, user.UserID.Userlongitude)<rad:
				result_users.append(user)

		serializer = OrderSerializer(result_users, many=True)
		return Response(serializer.data)

@api_view(['GET'])
def order_by_id(request):
	if request.method == 'GET':
		oid = int(request.query_params['orderId'])
		orders = OrderItems.objects.filter(OrderID=oid)
		serializer = OrderItemSerializer(orders, many=True)
		return Response(serializer.data)

@api_view(['GET'])
def create_data(request):
	if request.method == 'GET':
		num_users = 100

		for j in range(num_users):
			phonenumber = '99' + ''.join(random.choice("0123456789") for _ in range(6))
			username = names.get_first_name()
			print(phonenumber, username)
			user = User(Userlatitude=np.random.normal(35.15938300, 0.1), Userlongitude=np.random.normal(33.39632500, 0.1), Userphonenumber=phonenumber, UserName=username)
			user.save()

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
			
		
		return Response("Done")
