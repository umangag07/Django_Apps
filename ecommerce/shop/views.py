from django.shortcuts import render
from django.http import HttpResponse
from .models import product,user_contact
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
    return render(request, "shop/checkout.html")


def cart(request):
    return render(request, "shop/cart.html")

"""
// function to clear the cart items
  function clearcart(){
      cart=JSON.parse(localStorage.getItem('cart'));
      for(var item in cart){
          document.getElementById('val'+item).innerHTML= '<button id="'+item+'" type="button" class="btn btn-primary cart">Add to cart</button'>
      }
      localstore.clear();
      cart={};
      updatecart(cart);}
      popStr=popStr+"<a href='/shop/checkout'><button class='btn btn-primary' id='checkout'>Checkout</button></a> <button class='btn btn-primary' id='clearcart' oncli>Checkout</button>";
  }
"""    

