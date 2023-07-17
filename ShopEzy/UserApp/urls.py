from django.urls import path
from UserApp import views



urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("signin", views.signin, name="signin"),
    path("signin_admin", views.signin_admin, name="signin_admin"),
    path("manager_admin", views.manager_admin, name="manager_admin"),
    path("products/<int:context>/", views.products, name="products"),
    path("products_garments", views.products_garments, name="products_garments"),
    path("products_groceries", views.products_groceries, name="products_groceries"),
    path("cart", views.cart, name="cart"),
    path("checkout", views.checkout, name="checkout"),
    path("details", views.details, name="details"),
    path("details_manager", views.details_manager, name="details_manager"),
    path("details_supervisor", views.details_supervisor, name="details_supervisor"),
    path("details_stockclerk", views.details_stockclerk, name="details_stockclerk"),
    path("contact", views.contact, name="contact"),
    path("profile_customer", views.profile_customer, name="profile_customer"),
    path("profile_admin", views.profile_admin, name="profile_admin"),
    path("shopping_history", views.shopping_history, name="shopping_history"),
]