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
    if request.method=="POST":
        product=ProductForm(request.POST,request.FILES)
        if product.is_valid():
            product.save()
            return render(request,"createproduct.html",{"productform":ProductForm(),"message":"Your product has been created!"})
    else:
        product=ProductForm()
    return render(request,'createproduct.html',{'productform':product})