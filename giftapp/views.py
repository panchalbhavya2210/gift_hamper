from django.shortcuts import render
from .models import usertable

# Create your views here.

def viewPage(request):
    return render(request, "base.html")
def loginpage(request):
    return render(request, "login.html")
def signUp(request):
    return render(request, "signup.html")
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
        
        insertData = usertable(u_name=user_name, u_email=user_email, u_password=user_password, u_phone=user_phone, u_status = 0)
        insertData.save()
    return render(request, "base.html")