from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection


# Create your views here.
def index(request):
    # Render the HTML template index.html
    return render(request, 'UserApp/index.html')

def signin(request):
    # Render the HTML template signin.html
    if request.method == "POST":
        data = request.POST
        if len(data) == 3:
            email = data["email"]
            password = data["password"]
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM CUSTOMERS WHERE CEMAIL=%s AND CPASSWORD=%s", [email, password])
                row = cursor.fetchone()
                if row is not None:
                    return render(request, 'UserApp/products.html')
    return render(request, 'UserApp/signin.html')

def products(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM products")
        row = cursor.fetchall()
        print(row)
    # Render the HTML template products.html
    return render(request, 'UserApp/products.html')

def cart(request):
    # Render the HTML template cart.html
    return render(request, 'UserApp/cart.html')

def checkout(request):
    # Render the HTML template checkout.html
    return render(request, 'UserApp/checkout.html')

def product_details(request):
    # Render the HTML template product_details.html
    return render(request, 'UserApp/product_details.html')

def contact(request):
    # Render the HTML template contact.html
    return render(request, 'UserApp/contact.html')

def signin_admin(request):
    # Render the HTML template signin_admin.html
    if request.method == "POST":
        data = request.POST
        if len(data) == 4:
            email = data["email"]
            password = data["password"]
            passcode = data["passcode"]
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM ADMINISTRATORS WHERE AEMAIL=%s AND APASSWORD=%s AND PASSCODE=%s", [email, password, passcode])
                row = cursor.fetchone()
                if row is not None:
                    return render(request, 'UserApp/products.html')
        elif len(data) == 7:
            name = data["name"]
            email = data["email"]
            job = data["job"]
            passcode = data["passcode"]
            password = data["password"]
            confirm_password = data["password_2"]
            if password == confirm_password:
                with connection.cursor() as cursor:
                    cursor.execute("INSERT INTO ADMINISTRATORS (ANAME, AEMAIL, AJOB, APASSWORD, PASSCODE) VALUES (%s, %s, %s, %s, %s)", [name, email, job, password, passcode])
    return render(request, 'UserApp/signin_admin.html')