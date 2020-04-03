from django.contrib import admin
from backend.models import *

class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType
    list_display = ['ProductTypeName', 'get_name', ]

    def get_name(self, obj):
        if obj.CategoryID !=None:
            return obj.CategoryID.CategoryName
        return "None yet"
    get_name.short_description = 'Category'  #Renames column head

class CategoryAdmin(admin.ModelAdmin):
    model = ProductType
    list_display = ['CategoryID', 'CategoryName']

class PriceAdmin(admin.ModelAdmin):
    model = Price
    list_display = ['PriceID', 'ProductID', 'ShopID']

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['ProductID', 'ProductTypeID', 'ProductName', 'ProductQuantity', 'ProductBarcode']

class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ["UserID", "UserName", "Userphonenumber"]

class PastOrderAdmin(admin.ModelAdmin):
    model = User
    list_display = ["OrderID", "UserID", "OrderDelivered"]

admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Shop)
admin.site.register(ShopType)
admin.site.register(PastOrder, PastOrderAdmin)
admin.site.register(OrderItems)
admin.site.register(Price, PriceAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(User, UserAdmin)
