from django.urls import path
from UserApp import views



urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("signin", views.signin, name="signin"),
    path("signin_admin", views.signin_admin, name="signin_admin"),
    path("admin", views.admin, name="admin"),
    path("products", views.products, name="products"),
    path("cart", views.cart, name="cart"),
    path("checkout", views.checkout, name="checkout"),
    path("details", views.details, name="details"),
    path("contact", views.contact, name="contact"),
]