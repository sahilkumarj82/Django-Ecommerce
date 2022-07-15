from distutils.command.upload import upload
from pydoc import describe
from pyexpat import model
from statistics import mode
from telnetlib import STATUS
from unicodedata import category
from django.db import models

# Create your models here.
# Model for Category
class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=200)
    slug = models.TextField(unique = True)

    def __str__(self):
        return self.name

#Model for Subcategory of Category
class SubCategory(models.Model):
    name = models.CharField(max_length = 100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    icon = models.CharField(max_length=200,blank=True)
    slug = models.TextField(unique = True)

    def __str__(self):
        return self.name
#Model for Slider
STATUS = (('active','Active'),('','Default'))
class Slider(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'media')#upload Image code
    text = models.TextField(blank = True)
    rank = models.IntegerField()
    status = models.CharField(choices= STATUS,blank=True,max_length=100)

    def __str__ (self):
        return self.name

#Model for Ads
class Ad(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'media')
    text = models.TextField(blank=True)
    rank = models.IntegerField()
    def __str__(self):
        return self.name

#models for brand
class Brand(models.Model):
    name = models.CharField(max_length=400)
    image = models.ImageField(upload_to = 'media')
    rank = models.IntegerField()

    def __str__(self):
        return self.name

#for product
LABELS = (('new','New'),('hot','Hot'),('sale','Sale'),('','default'))
STOCK = (('In Stock','In Stock'),('Out Stock','Out Stock'))
class Product(models.Model):
    name = models.CharField(max_length=400)
    price = models.IntegerField()
    discount_price = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'media')#upload Image code
    description = models.TextField(blank = True)
    specification = models.TextField(blank=True)
    slug = models.TextField(unique = True)
    labels = models.CharField(choices= LABELS,max_length=100)
    stock = models.CharField(choices= STOCK,max_length=100)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class Review(models.Model):
    name = models.CharField(max_length=400)
    email = models.EmailField(max_length=400)
    Review = models.TextField(blank=True)
    slug = models.TextField()
    date = models.CharField(max_length=400)

    def __str__(self):
        return self.name
