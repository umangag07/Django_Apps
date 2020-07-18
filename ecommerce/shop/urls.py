from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ShopHome'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('tracker/', views.tracker, name='tracker'),
    path('search/',views.search,name='search'),
    path('productview/<int:myid>', views.productview, name='productview'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/',views.cart,name='cart')
]