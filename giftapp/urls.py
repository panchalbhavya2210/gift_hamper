from django.urls import path
from .import views

urlpatterns = [
    path("", views.viewPage, name="base"),
    path("about", views.aboutPage, name="about"),
    path('insert', views.registerUser, name='insert'),
    path("signup", views.signUp, name="signup"),
    path("login", views.login, name="login"),
    path('login_user', views.checklogin, name="login_user"),
    path("logout", views.logOutUser, name="logout"),
    path("cart", views.cartPage, name="cart"),
    path("checkout", views.checkoutPage, name="checkout"),
    path("contact", views.contactPage, name="contact"),
    path("product-details/<int:id>", views.prodDetails, name="product-details"),
    path("shop", views.shopPage, name="shop"),
    path("under-construction", views.underConsPage, name="under-construction"),
    path("wishlist", views.wishList, name="wishlist"),
    path("blog", views.blogPage, name="blog"),
    path("blog-details", views.blogList, name="blog-details"),
    path("addproduct", views.addproductpage, name="addproduct"),
    path('insertproductdata', views.insertproductdata, name="insertproductdata"),
    path("addproduct", views.addproductpage, name="addproduct"),
    path("manageproduct", views.manageproduct, name="manageproduct"),
    path("addwishlist/<int:id>", views.addToWishList, name="addwishlist"),
    path("addtocart/<int:id>", views.addTocart, name="addtocart"),
    
    path('deletewishlistitem/<int:id>', views.deleteWishlistItem, name="deletewishlistitem"),
    path('deleteproductdetail/<int:id>',views.deleteproductdetail, name="deleteproductdetail")
 ]
