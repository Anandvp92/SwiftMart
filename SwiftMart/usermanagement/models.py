from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self,email,phone_number,first_name,last_name,password=None,profile_pic=None,**extrafields):
        if not email:
            raise ValueError("Email is to be a valid")
        
        if not phone_number:
            raise ValueError("Phone number should be valid")
        
        email = self.normalize_email(email)

        user = self.model(first_name=first_name,last_name=last_name,email=email,phone_number=phone_number,profile_pic=profile_pic,**extrafields)

        user.set_password(password)

        user.save(using=self._db)

        return user


    def create_superuser(self,email,phone_number,first_name,last_name,password=None,profile_pic=None,**extrafields):
        extrafields.setdefault('is_superuser',True)
        return self.create_user(first_name=first_name,last_name=last_name,email=email,phone_number=phone_number,profile_pic=profile_pic,**extrafields)

class User(AbstractUser):

    username=None
    email=models.EmailField(('email address'),unique=True)
    phone_number=PhoneNumberField(('phone number'),unique=True)
    profile_pic=models.ImageField(('profile pic'),upload_to='static/ProfilePics/',blank=None,null=True)
    is_staff=models.BooleanField(('staff status'),default=True)
    is_active=models.BooleanField(('active status'),default=True)
    is_admin=models.BooleanField(('admin status'),default=False)
    last_login=models.DateTimeField(('Last Login Time Stamp'),auto_now=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name','phone_number']
    
    objects=UserManager()

    def __str__(self) -> str:
        return self.email


