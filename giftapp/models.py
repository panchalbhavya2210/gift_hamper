from email.policy import default
from random import choices
from django.db import models
from django.utils.safestring import mark_safe

U_STATUS = ((0, "Active"), (1, "Inactive"))
PRODUCT_STATUS = ((0, "Available"), (1, "Not Available"))
CART_STATUS = ((0, "Success"), (1, "Pending"))
ORDER_STATUS = ((0, "Delivered"), (1, "Pending"))
PAYMENT_STATUS = ((0, "Success"), (1, "Failed"))
RETURN_STATUS = ((0, "Returned"), (1, "Processing"))
COMPLAINT_STATUS = ((0, "Solved"), (1, "Pending"))


# Create your models here.

class usertable(models.Model):
    u_name=models.CharField(max_length=20)
    u_email=models.CharField(max_length=20)
    u_password=models.CharField(max_length=25)
    u_phone=models.BigIntegerField()
    u_status=models.IntegerField(choices=U_STATUS, default=0)

class userdeatiltable(models.Model):
    u_id = models.ForeignKey(usertable, on_delete=models.CASCADE)
    dob=models.DateField()
    u_address=models.TextField()
    u_image=models.ImageField(upload_to='photos')
    
    def U_Image(self):
        return mark_safe('<img src={} width="100"/>'.format(self.u_image.url))

class giftstockisttable(models.Model):
    name=models.CharField(max_length=15)
    password=models.CharField(max_length=15)
    email=models.CharField(max_length=20)
    phone_no=models.IntegerField()
    address=models.TextField(max_length=40)
    stockist_image=models.ImageField(upload_to='photos')
    def Stockist_Image(self):
           return mark_safe('<img src={} width="100"/>'.format(self.stockist_image.url))

class categorytable(models.Model):
    category_name=models.CharField(max_length=15)

class producttable(models.Model):
    catid = models.ForeignKey(categorytable, on_delete=models.CASCADE)
    stockist_id = models.ForeignKey(giftstockisttable, on_delete=models.CASCADE)
    p_name=models.CharField(max_length=15)
    p_description=models.CharField(max_length=25)
    p_image=models.ImageField(upload_to='photos')
    p_quantity=models.IntegerField()
    p_price=models.BigIntegerField()
    p_status=models.IntegerField(choices=PRODUCT_STATUS, default=0)
    def P_Image(self):
        return mark_safe('<img src={} width="100"/>'.format(self.p_image.url))

class carttable(models.Model):
    userid = models.ForeignKey(usertable, on_delete=models.CASCADE)
    product_id = models.ForeignKey(producttable, on_delete=models.CASCADE)
    c_quantity = models.IntegerField()
    total_amount=models.IntegerField()
    status=models.IntegerField(choices=CART_STATUS, default=1)
    
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
    user_id = models.ForeignKey(usertable, on_delete=models.CASCADE)
    p_id = models.ForeignKey(producttable, on_delete=models.CASCADE)
    comment=models.TextField()
    rating=models.IntegerField()

class complaintable(models.Model):
    u_id = models.ForeignKey(usertable, on_delete=models.CASCADE)
    comment=models.TextField()
    complain_status=models.IntegerField(choices=COMPLAINT_STATUS)
    complain_date=models.DateField()