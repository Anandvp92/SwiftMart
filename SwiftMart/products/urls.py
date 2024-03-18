from django.urls import path

from .views import indexpage,contactpage,aboutpage,productlist,cartpage,createproduct

urlpatterns=[
    path('index/',indexpage,name='indexpage'),
    path('contact/',contactpage,name='contactpage'),
    path('about/',aboutpage,name='aboutpage'),
    path('cart/',cartpage,name='cartpage'),
    path('create/',createproduct,name='createproduct'),
    path('product/',productlist,name='productlist'),
]