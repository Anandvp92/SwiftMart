from django.shortcuts import render,redirect
from .forms import UserForm,LoginForm
from .models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method=="POST":
       user=UserForm(request.POST)
       if user.is_valid():
           password=user.cleaned_data['password']
           confirm_password=user.cleaned_data['confirm_password']
           if password!=confirm_password:
               raise ValueError("Password is not matching")
           newuser=user.save(commit=False) 
           newuser.set_password(user.cleaned_data.get('password'))
           newuser.save()
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
          auth=authenticate(username=email,password=password)
          if auth:
              login(request,auth)
              return redirect('indexpage')
    else:
        user=LoginForm()
    return render(request,'login.html',{'userform':user})


@login_required
def indexpage(request):
    return render(request,'index.html')



def logoutuser(request):
    logout(request)
    return redirect('login')