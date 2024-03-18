from django.shortcuts import render,redirect
from .forms import UserForm,LoginForm
from .models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method=="POST":
       user=UserForm(request.POST,request.FILES)
       if user.is_valid():
            password=user.cleaned_data['password']
            confirm_password=user.cleaned_data['confirm_password']
            if password!=confirm_password:
                user.add_error("confirm_password","Password is not matching")
            else:
                newuser=user.save(commit=False) 
                newuser.set_password(user.cleaned_data.get('password'))
                newuser.save()
                messages.success(request,"User is created Please Login")
                return redirect('login')
    else:
        user=UserForm()
    return render (request,'register.html',{'userform':user})


def loginuser(request):
    if request.method=="POST":        
        user=LoginForm(request.POST)
        if user.is_valid():
          email=user.cleaned_data.get('email')  
          password=user.cleaned_data.get('password')
        if User.objects.filter(email=email).exists():
            auth=authenticate(username=email,password=password)           
            if auth is not None:
                login(request,auth)
                return redirect('indexpage')    
        else:
            messages.warning(request,"Email id or password is wrong")
        
            return render(request,'login.html',{'userform':user})        
    else:
        user=LoginForm()
    return render(request,'login.html',{'userform':user})


@login_required
def logoutuser(request):
    logout(request)
    return redirect('login')


def restpassword(request):
    return render(request,'resetpassword.html',{})