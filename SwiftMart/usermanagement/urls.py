from django.urls import path
from .views import register,loginuser,logoutuser,restpassword
urlpatterns=[
    path('register/',register,name='register'),
    path('login/',loginuser,name='login'),
    path('logout/',logoutuser,name='logoutuser'),
    path('resetpass/',restpassword,name='resetpass'),
]