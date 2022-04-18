from aaltu.models.customer import Customer
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from aaltu.models.product import Products
from aaltu.models.category import Category 
from django.views import View

class Index(View):
    def post(self,request):            
        item=request.POST.get('item')    
        cart=request.session.get('cart')   
        remove=request.POST.get('remove')    
        if cart:
            quantity=cart.get(item)
            if quantity:
                if remove:
                    if quantity==1:
                        cart.pop(item)
                    else:
                        cart[item]=quantity-1   
                else:
                    cart[item]=quantity+1
            else:
                cart[item]=1
        else:
            cart={}
            cart[item]=1
        request.session['cart']=cart
        # print(request.session['cart'])
        return redirect('homepage')
        
    def get(self,request):
        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}
        prod=None
        # request.session.get('cart').clear()
        categ=Category.get_all_categories()
        CategoryID= request.GET.get('category')
        if CategoryID:
        
            prod=Products.get_all_product_by_catogeryid(CategoryID)
        else :
            prod=Products.get_all_Products()
        data={}
        data['Product']=prod
        data['categories']=categ
        print('you are:',request.session.get('customer'))
        return render(request,'index.html',data)

        





# def index(request):
#     prod=None
#     categ=Category.get_all_categories()
#     CategoryID= request.GET.get('category')
#     if CategoryID:
        
#         prod=Products.get_all_product_by_catogeryid(CategoryID)
#     else :
#         prod=Products.get_all_Products()
#     data={}
#     data['Product']=prod
#     data['categories']=categ
#     print(request.session.get('email'))
#     return render(request,'index.html',data)