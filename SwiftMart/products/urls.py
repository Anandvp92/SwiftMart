from django.urls import path

from .views import indexpage,contactpage,aboutpage,productlist,cartpage

urlpatterns=[
    path('index/',indexpage,name='indexpage'),
    path('contact/',contactpage,name='contactpage'),
    path('about/',aboutpage,name='aboutpage'),
    path('cart/',cartpage,name='cartpage'),
    path('product/',productlist,name='productlist'),
]