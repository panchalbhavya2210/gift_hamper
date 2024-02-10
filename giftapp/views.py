from email.mime import base
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import *

# Create your views here.

def viewPage(request):
    return render(request, "base.html")
def signUp(request):
    return render(request, "signup.html")
def login(request):
    return render(request, "login.html")
def signUpSeller(request):
    return render(request, 'reg_seller.html')
def loginSeller(request):
    return render(request, "login_seller.html")
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
def blogPage(request):
    return render(request, "blog.html")
def blogList(request):
    return render(request, "blog-details.html")
def addproductpage(request):
    return render(request, "addproduct.html")
def manageproduct(request):
    return render(request, "manageproduct.html")


def registerUser(request):
    if request.method == "POST":
        user_name = request.POST.get('name')
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')
        user_phone = request.POST.get('ph_number')
        user_type = request.POST.get('type')
        user_dob = request.POST.get('date')
        user_image = request.FILES['uImage']
        
        insertData = usertable(u_name=user_name, u_email=user_email, u_password=user_password, u_phone=user_phone, u_status=0,u_type = user_type, u_image=user_image, dob=user_dob, is_verified=False, comments="")
        insertData.save()

        # Redirect to a success page
        return redirect(reverse('base'))

    return render(request, "index.html")




def checklogin(request):
# +    """
# +    Check user login credentials and redirect based on the result.
# +    Parameters:
# +        request: The HTTP request object containing user input.
# +
# +    Returns:
# +        If login is successful, redirects to the 'base' URL. If login fails, redirects to the 'login' URL.
# +    """
    useremail=request.POST["email"]
    userpaswd=request.POST["password"]
    try:
        query=usertable.objects.get(u_email=useremail,u_password=userpaswd)
        request.session['u_email']=query.u_email 
        request.session['u_id']=query.id #type:ignore
        messages.success(request, "Logged In Successfully.")
    except usertable.DoesNotExist:
        query=None
    if query is not None:
        return redirect(reverse('base'))
    else:
        messages.info(request, 'Incorrect email or password. Please try again.')
    return redirect(reverse('login'))


def logOutUser(request):
    # Clear the relevant session variables for logout
    request.session.pop('u_email', None)
    request.session.pop('u_id', None)
    request.session.pop('u_image', None)
    messages.success(request, "Logged out successfully.")
    return redirect(reverse('base'))


def insertproductdata(request):
    if request.method == 'POST':
        productname = request.POST.get("pname")
        productdescription = request.POST.get("pdesc")
        productimage = request.POST.get("pimage")
        productquantity = request.POST.get("pquantity")
        productprice = request.POST.get("pprice")
        productstatus = request.POST.get("pstatus")

        insertdata= producttable(p_name=productname, p_description=productdescription, p_image=productimage, p_quantity=productquantity, p_price=productprice, p_status=productstatus)
        insertdata.save()
    return redirect(reverse('base'))

