from django.contrib import admin
from .models import product,user_contact,order_details

# Register your models here.
admin.site.register(product)
admin.site.register(user_contact)
admin.site.register(order_details)