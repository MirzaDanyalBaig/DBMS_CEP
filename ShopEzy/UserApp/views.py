from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection


# Create your views here.
def index(request):
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'UserApp/index.html')

def signin(request):
    # Render the HTML template signin.html with the data in the context variable
    return render(request, 'UserApp/signin.html')

def signup(request):
    # Render the HTML template signup.html with the data in the context variable
    return render(request, 'UserApp/signup.html')


def cart(request):
    # Render the HTML template cart.html with the data in the context variable
    return render(request, 'UserApp/cart.html')

def checkout(request):
    return render(request, 'UserApp/checkout.html')

def product_details(request):
    return render(request, 'UserApp/product_details.html')

def contact(request):
    return render(request, 'UserApp/contact.html')

def admin_signin(request):
    return render(request, 'UserApp/admin_signin.html')

def admin_signup(request):
    return render(request, 'UserApp/admin_signup.html')