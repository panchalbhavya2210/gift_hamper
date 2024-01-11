from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.
class admin(models.Model):
    a_name=models.CharField(max_length=20)
    a_email=models.EmailField()
    a_password=models.CharField(max_length=20)
    a_phone=models.IntegerField()
    a_status=models.IntegerField()

class usertable(models.Model):
    u_name=models.CharField(max_length=20)
    u_email=models.CharField(max_length=20)
    u_password=models.CharField(max_length=25)
    u_phone=models.BigIntegerField()
    u_status=models.IntegerField()

class userdeatiltable(models.Model):
    # u_id=
    dob=models.DateField()
    u_address=models.CharField(max_length=100)
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
    # catid=
    # stockist_id=
    p_name=models.CharField(max_length=15)
    p_description=models.CharField(max_length=25)
    p_image=models.ImageField(upload_to='photos')
    p_quantity=models.IntegerField()
    p_price=models.BigIntegerField()
    p_status=models.IntegerField()
    def P_Image(self):
        return mark_safe('<img src={} width="100"/>'.format(self.p_image.url))

class carttable(models.Model):
    # userid=
    # product_id=
    # p_quantity=
    total_amount=models.IntegerField()
    status=models.CharField(max_length=20)

class ordertable(models.Model):
    # userid=
    # p_id=
    # cart_id=
    order_status=models.CharField(max_length=20)

class cardtable(models.Model):
    # u_id=
    card_name=models.CharField(max_length=20)
    cvv=models.IntegerField()
    expiry_date=models.DateField()
    card_number=models.BigIntegerField()
    payment_id=models.CharField(max_length=20)

class paymenttable(models.Model):
    # u_id=
    # order_id=
    payment_method=models.CharField(max_length=10)
    # total_amount=models.()
    payment_status=models.CharField(max_length=10)

class returnproducttablr(models.Model):
    # u_id=
    # payment_id=
    # order_id=
    date_of_return=models.DateField()
    return_status=models.CharField(max_length=15)

class feedbacktable(models.Model):
    # u_id=
    # p_id=
    comment=models.TextField()
    rating=models.IntegerField()

class complaintable(models.Model):
    # u_id=
    comment=models.TextField()
    complain_status=models.CharField(max_length=10)
    complain_date=models.DateField()


# y