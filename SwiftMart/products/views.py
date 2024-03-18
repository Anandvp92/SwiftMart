from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
# Create your views here.

def indexpage(request):
    return render(request,'index.html')



def contactpage(request):
    return render(request,'contact.html')



def aboutpage(request):
    return render(request,'about.html')


@login_required
def cartpage(request):
    return render(request,'cart.html')

@login_required
def productlist(request):
    return render(request,'productlist.html')


def createproduct(request):
    return render(request,'createproduct.html',{'productform':ProductForm})