import email
import imp
from django.shortcuts import redirect, render
from .models import *
from django.views.generic import View
import datetime
# Create your views here.

class Base(View): # --> Base for common page and View --> 
    views = {} #dict
    views['categories']  = Category.objects.all() # show all categories
    views['brands'] = Brand.objects.all() # get all slider and show
    all_brand  = []
    for i in Brand.objects.all():
        ids = Brand.objects.get(name = i).id
        count = Product.objects.filter(brand =ids).count()	
        all_brand.append({'product_count':count,'ids' : ids})

    views['counts'] = all_brand

    
class HomeView(Base):
    def get(self,request):
        self.views
        self.views['sliders'] = Slider.objects.all() # get all slider and show
        self.views['ads'] = Ad.objects.all() # get ads and show
        self.views['hots'] = Product.objects.filter(labels = 'hot') # filtering products from labels from models
        self.views['sales'] = Product.objects.filter(labels = 'sale') # filtering products from labels from models
        self.views['news'] = Product.objects.filter(labels = 'new') # filtering products from labels from models
        
        return render(request,'index.html',self.views) # --> for render

class ProductDetaileView(Base):
    def get(self,request,slug):
        self.views
        self.views['details'] = Product.objects.filter(slug = slug) 
        self.views['reviews'] = Product.objects.filter(slug = slug)
        subcat = Product.objects.get(slug = slug).sub_category
        
        self.views['subcat_products'] = Product.objects.filter(sub_category = subcat)
        return render(request,'product-detail.html',self.views)

def review(request,slug):
    if request.method == 'POST' :
        name = request.POST['name']
        email = request.POST['email']
        review = request.POST['review']
        x = datetime.datetime.now()
        date = x.strftime("%c")
        data = Review.objects.create(

            name = name,
            email = email,
            review = review,
            date = date,
            slug = slug
        )     
        data.save()   
        
    return redirect(f'/details/{slug}')


class CategoryView(Base):
    def get(self,request,slug):
        self.views
        cat_id = Category.objects.get(slug=slug).id
        self.views['cat_product'] = Product.objects.filter(category_id = cat_id)
        return render(request, 'product-list.html',self.views)
