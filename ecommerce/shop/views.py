
from django.shortcuts import render
from django.http import HttpResponse
from .models import product
from math import ceil
# Create your views here.


def index(request):
    allproducts=[]
    category=product.objects.values('product_category','id')
    allcategory={cat['product_category'] for cat in category}
    for cat in allcategory:
        prod=product.objects.filter(product_category=cat)       
        n=len(prod)
        nslide=n//4+ceil((n/4)-(n//4)) 
        allproducts.append([prod,range(1,nslide),nslide]) 
    allprod={'allproducts':allproducts}
    return render(request, 'shop/index.html',allprod)


def about(request):
    return render(request,'shop/about.html')


def contact(request):
    return HttpResponse("we are at contact")


def tracker(request):
    return HttpResponse("we are at tracker ")


def search(request):
    return HttpResponse("we are at search")


def productview(request):
     return HttpResponse("we are at product view")

def checkout(request):
    return HttpResponse("we are at checkout")
