from django.urls import path
from UserApp import views



urlpatterns = [
    path("", views.index, name="ShopEzy - Shopping Made Easier"),
    path("index", views.index, name="ShopEzy - Shopping Made Easier"),
    path("signin", views.signin, name="ShopEzy - Shopping Made Easier"),
    path("signin_admin", views.signin_admin, name="ShopEzy - Shopping Made Easier"),
    path("cart", views.cart, name="ShopEzy - Shopping Made Easier"),
    path("checkout", views.checkout, name="ShopEzy - Shopping Made Easier"),
    path("product_details", views.product_details, name="ShopEzy - Shopping Made Easier"),
    path("contact", views.contact, name="ShopEzy - Shopping Made Easier"),
]