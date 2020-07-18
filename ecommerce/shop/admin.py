from django.contrib import admin
from .models import product,user_contact

# Register your models here.
admin.site.register(product)
admin.site.register(user_contact)