from django.contrib import admin
from django.urls import path
from .views.home import Index
from .views.signup import Signup
from .views.login import Login,logout
from .views.cart import Cart
from .views.checkout import Checkout
from .views.order import OrderView
from .middleware.auth import auth_middleware


urlpatterns=[
      path('',Index.as_view(),name='homepage'),
      path('signup',Signup.as_view(),name='signup'),
      path('login',Login.as_view(),name='login'),
      path('logout',logout,name='logout'),
      path('Cart',Cart.as_view(),name='cart'),
      path('checkout',Checkout.as_view(),name='checkout'),
      path('order',auth_middleware(OrderView.as_view()),name='order'),



]