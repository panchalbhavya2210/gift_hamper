from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
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
        return redirect(reverse('base'))

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
        request.session['u_image'] = query.u_image.url if query.u_image else None
        messages.success(request, "Logged In Successfully.")
        print( request.session['u_image'])
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
    request.session.pop('seller_email', None)
    request.session.pop('seller_id', None)
    request.session.pop('seller_image', None)
    messages.success(request, "Logged out successfully.")
    return redirect(reverse('base'))

def checkSellerLogin(request):
    seller_email=request.POST["email"]
    seller_paswd=request.POST["password"]

    try:
        query=giftstockisttable.objects.get(email=seller_email,password=seller_paswd)
        request.session['seller_email']=query.email
        request.session['seller_id']=query.id #type:ignore
        request.session['seller_image'] = query.stockist_image.url if query.stockist_image else None
        messages.success(request, "Logged In Successfully.")
        print( request.session['seller_image'])
    except usertable.DoesNotExist:
        query=None
    if query is not None:
        return redirect(reverse('base'))
    else:
        messages.info(request, 'Incorrect email or password. Please try again.')
    return redirect(reverse('login_seller'))
