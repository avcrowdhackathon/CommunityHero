# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' Order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to reName the models, but don't reName db_table values or field Names.
from django.db import models


class Brand(models.Model):
    BrandID = models.AutoField(db_column='BrandID', primary_key=True)  # Field Name made lowercase.
    BrandName = models.CharField(db_column='BrandName', max_length=45)  # Field Name made lowercase.

    class Meta:
        db_table = 'Brand'

class Category(models.Model):
    CategoryID = models.AutoField(db_column='CategoryID', primary_key=True)  # Field Name made lowercase.
    CategoryName = models.CharField(db_column='CategoryName', max_length=45)  # Field Name made lowercase.

    class Meta:
        db_table = 'Category'

class PastOrder(models.Model):
    OrderID = models.AutoField(db_column='OrderID', primary_key=True)  # Field Name made lowercase.
    UserID = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field Name made lowercase.
    OrderDelivered = models.BooleanField(db_column='OrderDelivered')  # Field Name made lowercase.
    OrderTimestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'PastOrder'

class OrderItems(models.Model):
    OrderItemID = models.AutoField(db_column='OrderItemID', primary_key=True)  # Field Name made lowercase.
    OrderID = models.ForeignKey(PastOrder, models.DO_NOTHING, db_column='OrderID', blank=True, null=True)  # Field Name made lowercase.
    PriceID = models.ForeignKey('Price', models.DO_NOTHING, db_column='PriceID', blank=True, null=True)  # Field Name made lowercase.
    Quantity = models.DecimalField(db_column='Quantity', max_digits=4, decimal_places=2, blank=True, null=True)  # Field Name made lowercase.
    Notes = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        db_table = 'OrderItems'

class Price(models.Model):
    PriceID = models.AutoField(db_column='PriceID', primary_key=True)  # Field Name made lowercase.
    ShopID = models.ForeignKey('Shop', models.DO_NOTHING, db_column='ShopID', blank=True, null=True)  # Field Name made lowercase.
    ProductID = models.ForeignKey('Product', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field Name made lowercase.
    Price = models.DecimalField(db_column='Price', max_digits=8, decimal_places=2, blank=True, null=True)  # Field Name made lowercase.

    class Meta:
        db_table = 'Price'

class Product(models.Model):
    ProductID = models.AutoField(db_column='ProductID', primary_key=True)  # Field Name made lowercase.
    ProductTypeID = models.ForeignKey('ProductType', models.DO_NOTHING, db_column='ProductTypeID', blank=True, null=True)  # Field Name made lowercase.
    ProductName = models.CharField(db_column='ProductName', max_length=45, blank=True, null=True)  # Field Name made lowercase.
    ProductBrandID = models.ForeignKey(Brand, models.DO_NOTHING, db_column='ProductBrandID', blank=True, null=True)  # Field Name made lowercase.
    ProductQuantity = models.FloatField(db_column='ProductQuantity', blank=True, null=True)  # Field Name made lowercase.
    ProductUnit = models.CharField(db_column='ProductUnit', max_length=10, blank=True, null=True)  # Field Name made lowercase.
    ProductBarcode = models.CharField(db_column='ProductBarcode', max_length=18, blank=True, null=True)  # Field Name made lowercase.

    class Meta:
        db_table = 'Product'

class ProductType(models.Model):
    ProductTypeID = models.AutoField(db_column='ProductTypeID', primary_key=True)  # Field Name made lowercase.
    ProductTypeName = models.CharField(db_column='ProductTypeName', max_length=45)  # Field Name made lowercase.
    CategoryID = models.ForeignKey(Category, models.DO_NOTHING, db_column='CategoryID', blank=True, null=True)  # Field Name made lowercase.

    class Meta:
        db_table = 'ProductType'

class Shop(models.Model):
    ShopID = models.AutoField(db_column='ShopID', primary_key=True)  # Field Name made lowercase.
    ShopTypeID = models.ForeignKey('ShopType', models.DO_NOTHING, db_column='ShopTypeID')  # Field Name made lowercase.
    ShopName = models.CharField(db_column='ShopName', max_length=45)  # Field Name made lowercase.

    class Meta:
        db_table = 'Shop'

class ShopType(models.Model):
    ShopTypeID = models.AutoField(db_column='ShopTypeID', primary_key=True)  # Field Name made lowercase.
    ShopTypeName = models.CharField(db_column='ShopTypeName', max_length=45)  # Field Name made lowercase.

    class Meta:
        db_table = 'ShopType'

class ShoppingItem(models.Model):
    UserID = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field Name made lowercase.
    PriceID = models.ForeignKey(Price, models.DO_NOTHING, db_column='PriceID')  # Field Name made lowercase.
    Quantity = models.DecimalField(db_column='Quantity', max_digits=4, decimal_places=2, blank=True, null=True)  # Field Name made lowercase.
    ShoppingItemID = models.AutoField(db_column='ShoppingItemID', primary_key=True)  # Field Name made lowercase.
    Notes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'ShoppingItem'

class User(models.Model):
    UserID = models.AutoField(db_column='UserID', primary_key=True)  # Field Name made lowercase.
    UserName = models.CharField(db_column='UserName', max_length=45, blank=True, null=True)  # Field Name made lowercase.
    Userphonenumber = models.CharField(db_column='UserPhoneNumber', max_length=15, blank=True, null=True)  # Field Name made lowercase.
    Userlatitude = models.DecimalField(db_column='UserLatitude', max_digits=10, decimal_places=8, blank=True, null=True)  # Field Name made lowercase.
    Userlongitude = models.DecimalField(db_column='UserLongitude', max_digits=11, decimal_places=8, blank=True, null=True)  # Field Name made lowercase.

    class Meta:
        db_table = 'User'