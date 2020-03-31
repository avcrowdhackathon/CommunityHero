from backend.models import *
import time
f = open('../../products.txt')
for p in f:
    data = p.split(",")
    brand = data[1]
    product = data[0]
    brands = Brand.objects.filter(BrandName=brand)
    if len(brands)==0:
        brand = Brand(BrandName=brand)
        brand.save()
        brand_id = brand.BrandID

    brand_id = Brand.objects.filter(BrandName=data[1])[0]

    producttypes = ProductType.objects.filter(ProductTypeName=product)
    if len(producttypes)==0:
        producttype = ProductType(ProductTypeName=product)
        producttype.save()
    producttype_id = ProductType.objects.filter(ProductTypeName=data[0])[0]

    product = Product(ProductName=data[2], ProductTypeID=producttype_id, ProductBrandID=brand_id, ProductQuantity=data[3], ProductUnit=data[4], ProductBarcode=data[5].strip(' \n'))
    product.save()
