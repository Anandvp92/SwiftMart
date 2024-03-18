from django.forms import ModelForm
from .models import User
from django import forms

class UserForm(ModelForm):
    confirm_password=forms.CharField(widget=forms.PasswordInput,required=True,label="Confirm Password")
    class Meta:    
        model= User            
        fields=["first_name","last_name","email","phone_number","profile_pic","password"]
        widgets={"password":forms.PasswordInput}    
    
      
       
        
class LoginForm(forms.Form):

        email=forms.EmailField(label="Email",required=True)
        password=forms.CharField(label="Password",widget=forms.PasswordInput(),required=True)
