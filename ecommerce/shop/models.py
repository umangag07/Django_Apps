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
