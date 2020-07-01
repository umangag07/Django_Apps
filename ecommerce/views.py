
from django.shortcuts import render
from django.http import HttpResponse
from .models import product
from math import ceil
# Create your views here.


def index(request):
    products=product.objects.all()
    print(products)
    n=len(products)
    nslide=n//4+ceil((n/4)-(n//4)) 
    #prod={'no_of_slide':nslide,'product':products,'range':range(1,nslide)}
    allproducts=[[products,range(1,nslide),nslide],[products,range(1,nslide),nslide]]
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
