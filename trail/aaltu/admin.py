from aaltu.models.orders import Orders
from django.contrib import admin
from .models.product import Products
from .models.category import Category
from .models.customer import Customer

class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','category']


# Register your models here.
class AdminCategory(admin.ModelAdmin):
    list_display=['name']


admin.site.register(Products,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer)
admin.site.register(Orders)