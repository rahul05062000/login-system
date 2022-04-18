from django.db import models
from .category import Category

class Products(models.Model):
    name= models.CharField(max_length=225)
    price=models.IntegerField(default=0)
    category= models.ForeignKey(Category ,on_delete=models.CASCADE,default=1)
    discription=models.CharField(max_length=225)
    image=models.ImageField(upload_to='uploads/products/')


    @staticmethod
    def get_product_by_id(ids):
        return Products.objects.filter(id__in=ids)

    @staticmethod 
    def get_all_product_by_catogeryid(Category_id):
        return Products.objects.filter(category=Category_id)


    @staticmethod
    def get_all_Products():
        return Products.objects.all()