

from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from .models import *
from django.contrib import messages
from CRAFTER_app.forms import CustomUserForm
from django.contrib.auth import authenticate,login,logout
import json
# Create your views here.
def home(request):
    products=Product.objects.filter(trending=1)
    return render(request, 'CRAFTER_app/homepage.html',{'products':products})

def login_page(request):
    if request.user.is_authenticated:
       return redirect('homepage')
    else:
      if request.method=="POST":
        emailid=request.POST.get('email')
        pwd=request.POST.get('password')
        user=authenticate(request,email=emailid,password=pwd)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged in successfully")
            return redirect('homepage')
        else:
            messages.error(request,'Invalid Credentials')
            return render(request,'CRAFTER_app/login.html')
      return render(request,"CRAFTER_app/login.html")

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out successfully")
    return redirect('homepage')


def register(request):
  if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration success")
            return redirect('/login') 
  else:
        form = CustomUserForm()
  return render(request, 'CRAFTER_app/register.html', {'form': form})
def categories(request):
    category=Category.objects.filter(status=0)
    return render(request, 'CRAFTER_app/Categories.html',{'category':category})

def categoriesview(request,name):
    if(Category.objects.filter(name=name,status=0)):
        products=Product.objects.filter(category__name=name)
        return render(request, 'CRAFTER_app/products/index.html',{'products':products,'category_name':name})
    else:
        messages.warning(request,"No such Category Found")
        return redirect('categories')
    
def product_details(request,cname,pname):
    if(Category.objects.filter(name=cname,status=0)):
        if(Product.objects.filter(name=pname,status=0)):
            product=Product.objects.filter(name=pname,status=0).first()
            return render(request,"CRAFTER_app/products/pdetails.html",{"products":product})
        else:
            messages.error(request,"No such Product Found")
            return redirect('categories')
    else:
        messages.error(request,"No such Category Found")
        return redirect('categories')


def add_to_cart(request):
    if request.header.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_qty=data['product_qty']
            product_id=data['pid']
            product_status=Product.objects.get(id=product_id)
            if product_status:
                if Cart.objects.filter(user=request.user,product_id=product_id):
                    return JsonResponse({'status':'Already  in Cart'},status=200)
                else:
                    if product_status.quantity>=product_qty:
                        Cart.objects.create(user=request.user.id,product_id=product_id,product_qty=product_qty)
                        return JsonResponse({'status':'Added to Cart'},status=200)
                    else:
                        return JsonResponse({'status':'product out of stock  '},status=200)
        else:
            return JsonResponse({'status':'Login to Add  to Cart'},status=200)


    else:
        return JsonResponse({'status':'Invalid Access'},status=200)


def cart_page(request):
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
        return render(request,'CRAFTER_app/cart.html')
    else:
        return redirect('login')

def remove_cart(request,cid):
    cartitem=Cart.objects.get(id=cid)
    cartitem.delete()
    return redirect("/cart")



def homepage(request):
    return render(request,'CRAFTER_app/homepage.html')