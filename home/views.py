import email
import imp
from django.shortcuts import redirect, render
from .models import *
from django.views.generic import View
import datetime
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth import login,logout

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
        # name = request.POST['name']
        # email = request.POST['email']
        name = request.user.username
        email = request.user.email
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

class SearchView(Base):
    def get(self,request):
        self.views
        if request.method == 'GET':
            query = request.GET['query']
            self.views['search_product'] = Product.objects.filter(name__icontains = query)
            self.views['search_for'] = query
        return render(request, 'search.html',self.views)




def signup(request):

    if request.method == 'POST':
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:

            if User.objects.filter(username = username).exists(): #check whether user exits or not
                messages.error(request,"The Username is already taken")
                return redirect('/signup')

            elif User.objects.filter(email = email).exists():
                messages.error(request,"The email is already taken")
                return redirect('/signup')
            else:
                data = User.objects.create_user(
                    username = username,
                    email = email,
                    password = password,
                    first_name = f_name,
                    last_name = l_name
                )
                data.save()
                return redirect('/')

        else:
            messages.error(request,"The password does not match")
            return redirect('/signup')

    return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username,password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            messages.error(request,'The username or password doesnot match')
            return redirect('/login')

    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def cal(slug):
	price = Product.objects.get(slug = slug).price
	discount_price = Product.objects.get(slug = slug).discount_price
	if discount_price >0 :
		actual_price = discount_price
	else:
		actual_price = price
	try:
		quantity = Cart.objects.get(slug = slug).quantity
	except:
		return actual_price

	return quantity,actual_price

def add_to_cart(request,slug):
	username = request.user.username
	if Cart.objects.filter(slug = slug,username = username,checkout = False).exists():
		quantity,actual_price = cal(slug)
		quantity = quantity+1
		total = actual_price*quantity

		Cart.objects.filter(slug = slug,username = username,checkout = False).update(
			quantity = quantity,
			total = total
			)
	else:# when user added product for first time in cart
		actual_price= cal(slug)
		data = Cart.objects.create(
			username = username,
			slug = slug,
			total= actual_price,
			items = Product.objects.filter(slug = slug)[0]
			)
		data.save()
	return redirect('/my_cart')


def delete_cart(request,slug):
    username = request.user.username
    Cart.objects.filter(slug = slug,username = username , checkout = False).delete()
    return redirect('/my_cart')

def remove_cart(request,slug):
    username = request.user.username
    if Cart.objects.filter(slug = slug,username = username,checkout = False).exists():
        quantity,actual_price = cal(slug)
        if quantity>1:
            quantity = quantity-1
            total = actual_price*quantity

            Cart.objects.filter(slug = slug,username = username,checkout = False).update(
                quantity=quantity,
                total=total
            )
        return redirect('/my_cart')

class CartView(Base):
    def get(self,request):
        username = request.user.username
        self.views['my_cart'] = Cart.objects.filter(username = request.user.username, checkout = False)
        return render(request,'cart.html',self.views)








    