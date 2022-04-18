from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from aaltu.models.customer import Customer
from django.views import View


class Login(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        email= request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.get_customer_by_email(email)
        print(customer)
        error=None
        if customer:
            flag=check_password(password,customer.password)
            if flag:
                request.session['customer']=customer.id
                
                return redirect('homepage')
            else:
                error="invalid email or password"
        else:
            error="invalid email or password"
         
        # print(customer)
        # print(email,password)
        
        return  render(request,'login.html',{'error_message':error})

def logout(request):
    request.session.clear()
    return redirect('login')

