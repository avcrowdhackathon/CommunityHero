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

admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Shop)
admin.site.register(ShopType)
