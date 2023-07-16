from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
from UserApp.models import Products


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

def products(request):
    product_info = Products.objects.all()
    # with connection.cursor() as cursor:
    #     cursor.execute("SELECT * FROM product")
    #     row = cursor.fetchall()
    #     print(row)
    # Render the HTML template products.html with the data in the context variable
    return render(request, 'UserApp/products.html', {'product_info': product_info})

def cart(request):
    # Render the HTML template cart.html with the data in the context variable
    return render(request, 'UserApp/cart.html')

def checkout(request):
    return render(request, 'UserApp/checkout.html')

def details(request):
    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM product where product_id = {}", [request.GET.get('product_id')])
            row = cursor.fetchall()
            print(row)
    return render(request, 'UserApp/details.html')

def contact(request):
    return render(request, 'UserApp/contact.html')

def signin_admin(request):
    return render(request, 'UserApp/signin_admin.html')