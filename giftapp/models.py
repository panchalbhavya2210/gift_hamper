from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.safestring import mark_safe


U_STATUS = ((0, "Active"), (1, "Inactive"))
PRODUCT_STATUS = ((0, "Available"), (1, "Not Available"))
CART_STATUS = ((0, "Success"), (1, "Pending"))
ORDER_STATUS = ((0, "Delivered"), (1, "Pending"))
PAYMENT_STATUS = ((0, "Success"), (1, "Failed"))
RETURN_STATUS = ((0, "Returned"), (1, "Processing"))
COMPLAINT_STATUS = ((0, "Solved"), (1, "Pending"))
USER_TYPE = ((0, "User"), (1, "Seller"))

# Create your models here.

class usertable(models.Model):
    u_name=models.CharField(max_length=20)
    u_email=models.CharField(max_length=20)
    u_password=models.CharField(max_length=25)
    u_phone=models.BigIntegerField()
    u_status=models.IntegerField(choices=U_STATUS, default=0)
    u_image=models.ImageField()
    u_type=models.CharField(max_length=10)
    dob=models.DateField()
    is_verified=models.BooleanField(default=False)
    comments=models.CharField(max_length=100, default="")
    u_address=models.TextField(default="")

    def user_photo(self):
       return mark_safe('<img src="{}" width="100"/>'.format(self.u_image.url))
   
    user_photo.allow_tags = True
    
    def __str__(self) -> str:
        return self.u_name

class categorytable(models.Model):
    category_name=models.CharField(max_length=25)
    
class producttable(models.Model):
    catid = models.ForeignKey(categorytable, on_delete=models.CASCADE)
    stockist_id = models.ForeignKey(usertable, on_delete=models.CASCADE)
    p_name=models.CharField(max_length=15)
    p_description=models.CharField(max_length=25)
    p_image=models.ImageField()
    p_quantity=models.IntegerField()
    p_price=models.BigIntegerField()
    p_status=models.IntegerField(choices=PRODUCT_STATUS, default=0)

    def product_photo(self):
       return mark_safe('<img src="{}" width="100"/>'.format(self.p_image.url))
   
class HamperTable(models.Model):
    hamper_name = models.CharField(max_length=200)
    hamper_price = models.IntegerField()
    seller_id = models.ForeignKey(usertable, on_delete=models.CASCADE)
    hamper_image = models.ImageField()
    is_active = models.BooleanField(default=True)
    
    def hamper_image_display(self):
       return mark_safe('<img src="{}" width="100"/>'.format(self.hamper_image.url))
   
    hamper_image_display.allow_tags = True
    def __str__(self):
        return self.hamper_name
class carttable(models.Model):
    userid = models.ForeignKey(usertable, on_delete=models.CASCADE)
    product_id = models.ForeignKey(producttable, on_delete=models.CASCADE)
    c_quantity = models.IntegerField()
    total_amount=models.IntegerField(default=0)
    # status=models.IntegerField(choices=CART_STATUS, default=1)
    
class cardtable(models.Model):
    u_id = models.ForeignKey(usertable, on_delete=models.CASCADE)
    card_name=models.CharField(max_length=20)
    cvv=models.IntegerField()
    expiry_date=models.DateField()
    card_number=models.BigIntegerField()
class ordertable(models.Model):
    user_id = models.ForeignKey(usertable, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(carttable, on_delete=models.CASCADE)
    payment_method=models.CharField(max_length=10)
    total_amount=models.FloatField()
    order_status=models.IntegerField(choices=ORDER_STATUS, default=1)

class paymenttable(models.Model):
    u_id = models.ForeignKey(usertable, on_delete=models.CASCADE)
    order_id = models.ForeignKey(ordertable, on_delete=models.CASCADE)
    total_amount=models.BigIntegerField()
    payment_status=models.IntegerField(choices=PAYMENT_STATUS)


class returnproducttable(models.Model):
    u_id = models.ForeignKey(usertable, on_delete=models.CASCADE)
    payment_id = models.ForeignKey(paymenttable, on_delete=models.CASCADE)
    order_id = models.ForeignKey(ordertable, on_delete=models.CASCADE)
    date_of_return=models.DateField()
    return_status=models.IntegerField(choices=RETURN_STATUS)

class feedbacktable(models.Model):
    review_name = models.CharField(max_length=150, default='Default Review Name')
    user_id = models.ForeignKey(usertable, on_delete=models.CASCADE)
    p_id = models.ForeignKey(producttable, on_delete=models.CASCADE)
    comment=models.TextField()
    rating=models.IntegerField()
    submit_on = models.DateTimeField(auto_now=True)

class complaintable(models.Model):
    u_id = models.ForeignKey(usertable, on_delete=models.CASCADE)
    comment=models.TextField()
    complain_status=models.IntegerField(choices=COMPLAINT_STATUS)
    complain_date=models.DateTimeField(auto_now_add=True)
    
class wishlist(models.Model):
    u_id = models.ForeignKey(usertable, on_delete=models.CASCADE)
    p_id = models.ForeignKey(producttable, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
class multipleImage(models.Model):
    p_id = models.ForeignKey(producttable, on_delete=models.CASCADE)
    p_image=models.FileField()


class MultipleFeedBackImage(models.Model):
    f_id = models.ForeignKey(feedbacktable, on_delete=models.CASCADE)
    f_image=models.FileField()