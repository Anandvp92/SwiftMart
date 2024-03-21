from django.forms import ModelForm
from .models import User
from django import forms

class UserForm(ModelForm):
    confirm_password=forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500','placeholder':'confirm password'}))    
    class Meta:
        model= User            
        fields=["first_name","last_name","email","phone_number","profile_pic","password"]
        
        
        widgets ={"password":forms.PasswordInput(attrs={'placeholder':'password'})
                  ,"first_name":forms.TextInput(attrs={'placeholder':'First Name'})
                  ,"last_name":forms.TextInput(attrs={'placeholder':'Last Name'})
                  ,"email":forms.EmailInput(attrs={'placeholder':'Email'})
                  ,"phone_number":forms.NumberInput(attrs={'placeholder':'Phone Number'})
                  ,"profile_pic":forms.FileInput(attrs={'placeholder':'Profile Pic'})
       
                  }
        
        
          
        
    
      
       
        
class LoginForm(forms.Form):

        email=forms.EmailField(label="Email",required=True,widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
        password=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'placeholder': '***********'}),required=True)
