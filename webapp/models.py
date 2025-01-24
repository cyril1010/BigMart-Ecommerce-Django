from django.db import models

class ContactDB(models.Model):
    name = models.CharField(max_length=30,null=True,blank=True)
    number = models.IntegerField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    message = models.TextField(null=True,blank=True)

class UserDB(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    username = models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    phone = models.CharField(max_length=15, blank=True)
    password = models.CharField(max_length=128)

class CartDB(models.Model):
    username = models.CharField(max_length=100,null=True,blank=True)
    ProductName = models.CharField(max_length=100,null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    TotalPrice = models.IntegerField(null=True,blank=True)
    Prod_Image = models.ImageField(upload_to="Cart Images",null=True,blank=True)

class OrderDB(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    place = models.CharField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    mobile = models.IntegerField(null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    pin = models.IntegerField(null=True,blank=True)
    total_price = models.IntegerField(null=True,blank=True)
    message = models.CharField(max_length=100,null=True,blank=True)











