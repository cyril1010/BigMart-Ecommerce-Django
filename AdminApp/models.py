from django.db import models

class CategoryDB(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='category_images/',null=True,blank=True)


class ProductDB(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

class Newsletter(models.Model):
    email = models.EmailField(null=True,blank=True)
