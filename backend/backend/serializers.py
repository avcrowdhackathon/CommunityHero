from rest_framework import serializers
from backend.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('CategoryID', 'CategoryName')

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ('ProductTypeID', 'ProductTypeName', 'CategoryID')
        depth = 2

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('ProductID', 'ProductName', 'ProductTypeID', 'ProductBrandID', 'ProductQuantity', 'ProductUnit', 'ProductBarcode')
        depth = 3

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastOrder
        fields = ('OrderID', 'UserID')
        depth = 2

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = ('OrderID', 'PriceID', 'Quantity', 'Notes')
        depth = 3
