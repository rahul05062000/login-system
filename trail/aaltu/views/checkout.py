from aaltu.models.orders import Orders
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from aaltu.models.customer import Customer
from django.views import View
from aaltu.models.product import Products


class Checkout(View):
    def post(self,request):
        address=request.POST.get('Address')
        phone=request.POST.get('phone')
        customer=request.session.get('customer')
        cart=request.session.get('cart')
        product=Products.get_product_by_id(list(cart.keys()))
        
        for product in product:
            order = Orders(
                         customer=Customer(id=customer),
                         product=product,
                         price=product.price,
                         address=address,
                         phone=phone,
                         quantity=cart.get((str(product.id)))
            )       
            request.session['cart']={}
            order.placeorder(); 
                    
        return redirect('cart')


