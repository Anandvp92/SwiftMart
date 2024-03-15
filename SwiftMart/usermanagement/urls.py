from django.urls import path
from .views import register,loginuser,indexpage,logoutuser
urlpatterns=[
    path('register/',register,name='register'),
    path('login/',loginuser,name='login'),
    path('index/',indexpage,name='indexpage'),
    path('logout/',logoutuser,name='logoutuser'),
]