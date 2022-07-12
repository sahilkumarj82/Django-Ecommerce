import imp
from django.shortcuts import render
from .models import *
from django.views.generic import View
# Create your views here.

class Base(View): # --> Base for common page and View --> 
    views = {} # 
class HomeView(Base):
    def get(self,request):
        self.views['categories']  = Category.objects.all() # show all categories
        self.views['sliders'] = Slider.objects.all() # get all slider and show
        self.views['ads'] = Ad.objects.all() # get ads and show
        self.views['brands'] = Brand.objects.all() # get all slider and show
        self.views['hots'] = Product.objects.filter(labels = 'hot') # filtering products from labels from models
        self.views['sales'] = Product.objects.filter(labels = 'sale') # filtering products from labels from models
        self.views['news'] = Product.objects.filter(labels = 'new') # filtering products from labels from models
        
        return render(request,'index.html',self.views) # --> for render

class ProductDetaileView(Base):
    def get(self,request,slug):
        self.views['detailes'] = Product.objects.filter(slug = slug)

        return render(request,'product-detail.html',self.views)