from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from aaltu.models.customer import Customer
from django.views import View
from aaltu.models.product import Products


class Cart(View):
    def get(self,request):
        ids=list(request.session.get('cart').keys())
        products=Products.get_product_by_id(ids)
        print(products)
        return render(request,'cart.html',{'item':products})
