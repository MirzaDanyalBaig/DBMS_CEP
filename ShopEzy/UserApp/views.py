from django.http import HttpResponse
from django.shortcuts import render
# from django.db import connection


# def my_custom_sql(self):
#     with connection.cursor() as cursor:
#         cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
#         cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
#         row = cursor.fetchone()

#     return row

# Create your views here.
def index(request):
    # return HttpResponse("Hello World")
    return render(request, 'UserApp/index.html')

def signin(request):
    return render(request, 'UserApp/signin.html')

def signup(request):
    return render(request, 'UserApp/signup.html')

def home(request):
    return render(request, 'UserApp/home.html')

def cart(request):
    return render(request, 'UserApp/cart.html')

def checkout(request):
    return render(request, 'UserApp/checkout.html')

def product_details(request):
    return render(request, 'UserApp/product-details.html')

def contact(request):
    return render(request, 'UserApp/contact.html')
