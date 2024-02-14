from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
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
    paginator = Paginator(prodData, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "shop.html", {'data':page_obj})
def underConsPage(request):
    return render(request, "under-construction.html")
def wishList(request):
    dataOfWish = wishlist.objects.filter(u_id=request.session.get('u_id'))
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
        sid=request.session['u_id']
        productname = request.POST.get("pname")
        productdescription = request.POST.get("pdesc")
        productimage = request.FILES["pimage"]
        productquantity = request.POST.get("pquantity")
        productprice = request.POST.get("pprice")
        productstatus = request.POST.get("pstatus")
        cat_id = request.POST.get("category")
      
        insertdata = producttable(catid=categorytable(id=cat_id),stockist_id=usertable(id=sid),p_name=productname, p_description=productdescription, p_image=productimage, p_quantity=productquantity, p_price=productprice, p_status=productstatus)
        insertdata.save()
    return redirect(reverse('base'))

def addToWishList(request, id):
    try:
        if wishlist.objects.filter(u_id=usertable(request.session['u_id']), p_id=producttable(id=id)).exists():
            messages.info(request,"Already Exist In Wishlist")
        else:
            insertdata = wishlist(p_id=producttable(id=id), u_id=usertable(request.session['u_id']))
            insertdata.save()
            messages.success(request, "Add to wishlist successfully.")
    except:
        pass
        messages.info(request, "User not logged in.")
    return redirect(reverse('base'))


def deleteWishlistItem(request, id):
    deleteItem = wishlist.objects.get(id=id)
    deleteItem.delete()
    return redirect('wishlist')

def deleteproductdetail(request, id):
    deleteItem = producttable.objects.get(id=id)
    deleteItem.delete()
    return redirect('manageproduct')