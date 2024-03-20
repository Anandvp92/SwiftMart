from django.forms import ModelForm
from .models import User
from django import forms

class UserForm(ModelForm):
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':''}),required=True,label="Confirm Password")
    class Meta:    
        model= User            
        fields=["first_name","last_name","email","phone_number","profile_pic","password"]
        widgets={"password":forms.PasswordInput(attrs={'class':'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'})}    
    
      
       
        
class LoginForm(forms.Form):

        email=forms.EmailField(label="Email",required=True)
        password=forms.CharField(label="Password",widget=forms.PasswordInput(),required=True)
