from django.shortcuts import render,redirect
from .forms import User_registration
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from pets.models import Pet
from django.contrib.auth.models import Group

# Create your views here.

def home_page(request):
    instance=Pet.pets.all()
    context={"title":'Pet store',
             'content':"This is home page",
             "object_list":instance
             }
    
    

    
    return render(request,'account/index.html',context=context)

def user_registration(request):
    print(request.method)
    form=User_registration()
    if request.method=="POST":
        print("POST:  ",request.POST)
        form=User_registration(request.POST)#we are creating form object with value 
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            form.save()
            
            group=Group.objects.get(name="customer")
            group.user_set.add(user)
            return redirect('/')
    return render(request,'account/signup.html',{'form':form})

def user_login(request):
    form=AuthenticationForm()
    if request.method == "POST":
        name=request.POST['username']
        pwd=request.POST.get('password')
        user=authenticate(username=name,password=pwd)#username ,password
        if user != None:
            login(request,user)
            print('user.....',request.user)
            return redirect('/')
        else: 
            msg='Enterd username or Password is wrong'
            return render(request,'account/login.html',{'form':form,"msg":msg})

        
    return render(request,'account/login.html',{'form':form})

def user_logout(request):
    print(request.user)
    print(request.user.is_authenticated)
    logout(request)
    print(request.user)
    return redirect('/')






