from django.shortcuts import render
from django.http import HttpResponse
from .models import product,user_contact,order_details
from math import ceil

# Create your views here.


def index(request):
    allproducts = []
    category = product.objects.values("product_category", "id")
    allcategory = {item["product_category"] for item in category}
    for cat in allcategory:
        prod = product.objects.filter(product_category=cat)
        n = len(prod)
        nslide = n // 4 + ceil((n / 4) - (n // 4))
        allproducts.append([prod, range(1, nslide), nslide])
    allprod = {"allproducts": allproducts}
    return render(request, "shop/index.html", allprod)


def about(request):
    return render(request, "shop/about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phoneno = request.POST.get("phoneno", "")
        desc = request.POST.get("desc", "")
        Contact = user_contact(name=name, email=email, phoneno=phoneno, desc=desc)
        Contact.save()
    return render(request, "shop/contact.html")


def tracker(request):
    return render(request, "shop/tracker.html")


def search(request):
    return render(request, "shop/search.html")


def productview(request, myid):
    prod = product.objects.filter(id=myid)
    return render(request, "shop/productview.html", {"product": prod[0]})


def checkout(request):
    if request.method=="POST":
        cust_item_json=request.POST.get("itemsjson",'')
        cust_fname=request.POST.get("fname","")
        cust_lname=request.POST.get("lname","")
        cust_email=request.POST.get("email","")
        cust_phoneno=request.POST.get("phoneno","")
        cust_address=request.POST.get("address","")
        cust_addressline2=request.POST.get("addressline2","")
        cust_city=request.POST.get("city","")
        cust_state=request.POST.get("state","")
        cust_zip=request.POST.get("zip","")
        Order_details=order_details(cust_item_json=cust_item_json,cust_fname=cust_fname,cust_lname=cust_lname,cust_email=cust_email,cust_phoneno=cust_phoneno,cust_address=cust_address,cust_addressline2=cust_addressline2,cust_city=cust_city,cust_state=cust_state,cust_zip=cust_zip)
        Order_details.save()
        thank=True    #for checking thta request is made 
        id=order_details.order_id
        return render(request, "shop/checkout.html",{'thank':thank,'id':id}) 
    return render(request, "shop/checkout.html")


def cart(request):
    return render(request, "shop/cart.html")

