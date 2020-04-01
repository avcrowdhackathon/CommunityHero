from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from backend.models import *
from backend.serializers import *
from django.db.models import Q

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

