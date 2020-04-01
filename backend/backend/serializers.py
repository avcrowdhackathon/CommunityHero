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

