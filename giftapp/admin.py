from re import A
from django.contrib import admin
from .models import *

# Register your models here.


class showUser(admin.ModelAdmin):
    list_display = ["u_name", "u_email","u_password", "u_phone", "u_status","u_type", "user_photo", "dob", "is_verified", "comments", "u_address"]
admin.site.register(usertable, showUser)

class showCategory(admin.ModelAdmin):
    list_display = ["category_name"]
admin.site.register(categorytable, showCategory)

class showProduct(admin.ModelAdmin):
    list_display = ["catid", "stockist_id", "p_name", "p_description", "p_image", "p_quantity", "p_price", "p_status"]
admin.site.register(producttable, showProduct)

class showCart(admin.ModelAdmin):
    list_display = ["userid", "product_id", "c_quantity"]
admin.site.register(carttable, showCart)

# class showCard(admin.ModelAdmin):
#     list_display = ["u_id", "card_name", "cvv", "expiry_date", "card_number"]
# admin.site.register(cardtable, showCard)

class showOrder(admin.ModelAdmin):
    list_display = ["user_id", "cart_id", "payment_method", "total_amount", "order_status"]
admin.site.register(ordertable, showOrder)

class showPayment(admin.ModelAdmin):
    list_display = ["u_id", "order_id", "total_amount", "payment_status"]
admin.site.register(paymenttable, showPayment)

class showReturnProduct(admin.ModelAdmin):
    list_display = ["u_id", "payment_id", "order_id", "date_of_return", "return_status"]
admin.site.register(returnproducttable, showReturnProduct)

class showFeedback(admin.ModelAdmin):
    list_display = ["user_id", "p_id", "comment", "rating"]
admin.site.register(feedbacktable, showFeedback)

class showComplaint(admin.ModelAdmin):
    list_display = ["u_id", "comment", "complain_status", "complain_date"]
admin.site.register(complaintable, showComplaint)


class showWishList(admin.ModelAdmin):
    list_display = ["u_id", "p_id", "created_at"]
admin.site.register(wishlist, showWishList)