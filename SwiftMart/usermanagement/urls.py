from django.urls import path
from .views import register,loginuser,logoutuser
urlpatterns=[
    path('register/',register,name='register'),
    path('login/',loginuser,name='login'),
    path('logout/',logoutuser,name='logoutuser'),
]