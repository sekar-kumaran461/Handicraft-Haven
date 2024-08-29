from django.db import models
from django.contrib.auth.models import User
import datetime
import os


def getFilename(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    # new_filename="%M%S"%(now_time,filename)
    new_filename = f"{now_time}{filename}"
    return os.path.join('uploads/',new_filename)

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=150,null=False,default='category')
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=getFilename,null=True,blank=True)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    trending=models.BooleanField(default=False,help_text="0-default,1-Trending")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=150,null=False,blank=False)
    product_image=models.ImageField(upload_to=getFilename,null=True,blank=True)
    brand=models.CharField(max_length=150,default="Brand",blank=False)
    quantity=models.IntegerField(null=False,blank=False)
    orignal_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    trending=models.BooleanField(default=False,help_text="0-default,1-Trending")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    @property
    def total_cost(self):
        return self.product_qty * self.product.selling_price



# Create your models here.
