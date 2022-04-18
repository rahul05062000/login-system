from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from aaltu.models.customer import Customer
from django.views import View



class Signup(View):
    
    def get(self,request):
        return render(request,'signup.html')
    def post(self, request):
        postdata=request.POST
        first_name=postdata.get('first_name')
        last_name=postdata.get('last_name')
        phone=postdata.get('phone')
        email= postdata.get('email')
        password=postdata.get('password')
        #validation
        customer=Customer(first_name=first_name,
                          last_name=last_name,
                          phone=phone,
                          email=email,
                          password=password)
        value = {
            'first_name':first_name,
            'last_name':last_name,
            'phone':phone,
            'email':email
        }    
        
        error=self.Validation(customer)
        #saving 
        if not error:
            customer.password=make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data= {
                'error_message':error,
                'values':value
            }
               
            return render(request,'signup.html',data)
    def Validation(self,customer):
        error=None
        if not customer.first_name:
            error="firstname fill please"
        elif len(customer.first_name)<4:
            error="first_name must be greater then four digit"
        
        if not customer.last_name:
            error="last name fill please"
        elif len(customer.last_name)<4:
            error="last name must be greater then four digit"

        if not customer.phone:
            error="phone number fill please"
        elif len(customer.phone)<10:
            error="phoenumber must be greater then ten digit"

        if not customer.password:
            error="password fill please"
        elif len(customer.password)<6:
            error="password must be greater then six digit"
        
        elif customer.Isexist():
            error="email already exist"
        return error