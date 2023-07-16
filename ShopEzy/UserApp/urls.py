from django.urls import path
from UserApp import views



urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("signin", views.signin, name="signin"),
    path("signin_admin", views.signin_admin, name="signin_admin"),
    path("manager_admin", views.manager_admin, name="manager_admin"),
    path("products", views.products, name="products"),
    path("products_garments", views.products_garments, name="products_garments"),
    path("products_groceries", views.products_groceries, name="products_groceries"),
    path("cart", views.cart, name="cart"),
    path("checkout", views.checkout, name="checkout"),
    path("details", views.details, name="details"),
    path("contact", views.contact, name="contact"),
    path("profile_customer", views.profile_customer, name="profile_customer"),
]