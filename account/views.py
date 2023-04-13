from django.shortcuts import render,redirect
from .models import Customer
from django.contrib.auth.hashers import make_password



def signup(request):
    if request.method == "GET":
        return render(request,'singup.html')
    

    else:
        data = request.POST
        full_name = data.get('full_name')
        email = data.get('email')
        mobile_no = data.get('mobile_no')
        create_password = data.get('create_password')
        repeat_password = data.get('repeat_password')
        print(full_name)
        print(len(create_password))
        print(repeat_password)

        error = None
        if create_password!= repeat_password:
            error = "password is invalid"
        elif len(full_name)<4:
            error = "full name is less then "
        
        if not error:

            customer = Customer(full_name=full_name,
                                email=email,
                                mobile_no = mobile_no,
                                create_password=create_password
                                )
            if Customer.objects.get(email = email):
                return render(request,'singup.html',{'error':"email is present"})


            else:
                customer.create_password = make_password(create_password)
                customer.save()

            return redirect('login')
        
        else:
            return render(request,'singup.html',{'error':error})


def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    
    else:
        data = request.POST
        email = data.get('email')
        password = data.get('password')
        customer = Customer.objects.filter(email=email,create_password=password).count()
        print(customer)
        if customer>0:
            request.session['login'] = True
            return redirect('index')
        else:
            return render(request,'login.html')
        

def logout(request):
    del request.session['login']
    return redirect('login')
            
