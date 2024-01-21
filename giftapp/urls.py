from django.urls import path
from .import views

urlpatterns = [
    path("", views.viewPage, name="base"),
    path("about", views.aboutPage, name="about"),
    path('insert', views.registerUser, name='insert'),
    path("signup", views.signUp, name="signup"),
    path("login", views.login, name="login"),
    path("register_seller", views.signUpSeller, name="register_seller"),
    path("insert_seller", views.registerSeller, name="insert_seller"),
    path("cart", views.cartPage, name="cart"),
    path("checkout", views.checkoutPage, name="checkout"),
    path("contact", views.contactPage, name="contact"),
    path("product-details", views.prodDetails, name="product-details"),
    path("shop", views.shopPage, name="shop"),
    path("under-construction", views.underConsPage, name="under-construction"),
    path("wishlist", views.wishList, name="wishlist"),
    path("blog", views.blogPage, name="blog"),
    path("blog-details", views.blogList, name="blog-details"),
]
