from webbrowser import get
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .models import *

# Create your views here.

def viewPage(request):
    prodData = producttable.objects.all()
    
    return render(request, "base.html", {'data':prodData})
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
def prodDetails(request, id):
    fetchProduct = producttable.objects.get(id=id)
    return render(request, "product-details.html", {'data':fetchProduct})
def shopPage(request):
    prodData = producttable.objects.all()
    return render(request, "shop.html", {'data':prodData})
def underConsPage(request):
    return render(request, "under-construction.html")
def wishList(request):
    # print(request.session.get('u_id'))
    dataOfWish = wishlist.objects.filter(u_id=request.session.get('u_id'))
    print(dataOfWish)
    return render(request, "wishlist.html", {'data':dataOfWish})
def blogPage(request):
    return render(request, "blog.html")
def blogList(request):
    return render(request, "blog-details.html")
def addproductpage(request):
    categData = categorytable.objects.all()
    return render(request, "addproduct.html", {'data':categData})
def manageproduct(request):
    productData = producttable.objects.all()
    return render(request, "manageproduct.html", {'data':productData})


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
        print(request.session['u_id'])
        messages.success(request, "Logged In Successfully.")
    except usertable.DoesNotExist:
        query=None
    if query is not None:
        return redirect(reverse('base'))
    else:
        messages.info(request, 'Incorrect email or password. Please try again.')
    return redirect(reverse('login'))



def logOutUser(request):
    request.session.pop('u_email', None)
    request.session.pop('u_id', None)
    request.session.pop('u_image', None)
    messages.success(request, "Logged out successfully.")
    return redirect(reverse('base'))



def insertproductdata(request):
# +    """
# +    A function to insert product data using the request object.
# +    """
    if request.method == 'POST':
        productname = request.POST.get("pname")
        productdescription = request.POST.get("pdesc")
        productimage = request.FILES["pimage"]
        productquantity = request.POST.get("pquantity")
        productprice = request.POST.get("pprice")
        productstatus = request.POST.get("pstatus")
        cat_id = request.POST.get("category")
      
        category_instance = get_object_or_404(categorytable, id=cat_id)
        stockist_id=43
        stockist_instance = get_object_or_404(usertable, id=stockist_id)
        insertdata = producttable(catid=category_instance,stockist_id=stockist_instance,p_name=productname, p_description=productdescription, p_image=productimage, p_quantity=productquantity, p_price=productprice, p_status=productstatus)
        insertdata.save()
    return redirect(reverse('base'))

def addToWishList(request, id):
    product = get_object_or_404(producttable, id=id)
    user = get_object_or_404(usertable, id=request.session.get('u_id'))
    insertdata = wishlist(p_id=product, u_id=user)
    insertdata.save()
    return redirect(reverse('base'))

