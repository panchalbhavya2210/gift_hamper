import imp
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from .models import usertable, giftstockisttable

# Create your views here.

def viewPage(request):
    return render(request, "base.html")
def signUp(request):
    return render(request, "signup.html")
def login(request):
    return render(request, "login.html")
def signUpSeller(request):
    return render(request, 'reg_seller.html')
def aboutPage(request):
    return render(request, "about.html")
def blogDetails(request):
    return render(request, "blog-details.html")
def cartPage(request):
    return render(request, "cart.html")
def checkoutPage(request):
    return render(request, "checkout.html")
def contactPage(request):
    return render(request, "contact.html")
def prodDetails(request):
    return render(request, "product-details.html")
def shopPage(request):
    return render(request, "shop.html")
def underConsPage(request):
    return render(request, "under-construction.html")
def wishList(request):
    return render(request, "wishlist.html")

def registerUser(request):
    if request.method == "POST":
        user_name = request.POST.get('name')
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')
        user_phone = request.POST.get('ph_number')
        user_image = request.FILES['uImage']
        
        insertData = usertable(u_name=user_name, u_email=user_email, u_password=user_password, u_phone=user_phone, u_status=0, u_image=user_image)
        insertData.save()

        # Redirect to a success page
        return redirect(reverse('insert'))

    return render(request, "index.html")


def registerSeller(request):
    if request.method == "POST":
        seller_name = request.POST.get('seller_name')
        seller_email = request.POST.get('seller_email')
        sller_ph_number = request.POST.get('seller_ph_number')
        seller_password = request.POST.get('seller_password')
        seller_address = request.POST.get('seller_address')
        seller_image = request.FILES['sImage']
        
        insertSellerData = giftstockisttable(name=seller_name, email=seller_email, password=seller_password, phone_no=sller_ph_number, address=seller_address, stockist_image=seller_image)
        insertSellerData.save()
        
        return redirect(reverse('insert_seller'))
    return render(request, 'index.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('login'))