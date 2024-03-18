from django.db import models

# Create your models here.

class Product(models.Model):
    title=models.CharField(("Title"),max_length=255)
    description=models.CharField(("Description"),max_length=200)
    price=models.DecimalField(("Price"),decimal_places=4,max_digits=5)
    product_image=models.ImageField(("productimage"),upload_to='static/productimage/',blank=True,null=True)
    
    