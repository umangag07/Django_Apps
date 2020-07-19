from django.db import models

# Create your models here.
class product(models.Model):
    product_name = models.CharField(max_length=30)
    product_desc = models.CharField(max_length=200)
    product_price=models.IntegerField()
    product_Pub_Date = models.DateField()
    product_category=models.CharField(max_length=20,default=" ")
    product_sub_category=models.CharField(max_length=40,default=" ")
    product_image=models.ImageField(upload_to="shop/images")

    def __str__(title):
        return title.product_name

class user_contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30, default='')
    phoneno=models.CharField(max_length=30,default='')
    desc=models.TextField(max_length=500,default='')

    def __str__(self):
            return self.name

class order_details(models.Model):
    order_id=models.AutoField(primary_key=True)
    cust_item_json=models.CharField(max_length=5000)
    cust_fname=models.CharField(max_length=50)
    cust_lname=models.CharField(max_length=50)
    cust_email=models.EmailField(max_length=50,default='')
    cust_phoneno=models.CharField(max_length=50,default='')
    cust_address=models.CharField(max_length=300,default='')
    cust_addressline2=models.CharField(max_length=300,default='')
    cust_city=models.CharField(max_length=40,default='')
    cust_state=models.CharField(max_length=30,default='')
    cust_zip=models.IntegerField()


