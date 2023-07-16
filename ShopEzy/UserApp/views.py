from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection

# with connection.cursor() as cursor:
#     cursor.execute("SELECT * FROM products")
#     rows = cursor.fetchall()
#     print(rows)

# Create your views here.
def index(request):
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'UserApp/index.html')

def signin(request):
    # Render the HTML template signin.html with the data in the context variable
    return render(request, 'UserApp/signin.html')

def products(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        # print(products)
        context = {'products': products,}
    return render(request, 'UserApp/products.html', context=context)

def products_garments(request):
    return render(request, 'UserApp/products_garments.html')

def products_groceries(request):
    return render(request, 'UserApp/products_groceries.html')

def cart(request):
    # Render the HTML template cart.html with the data in the context variable
    return render(request, 'UserApp/cart.html')

def checkout(request):
    # Render the HTML template checkout.html with the data in the context variable
    return render(request, 'UserApp/checkout.html')

def details(request):
    # if request.method == "GET":
    #     with connection.cursor() as cursor:
    #         cursor.execute("SELECT * FROM product where product_id = {}", [request.GET.get('product_id')])
    #         row = cursor.fetchall()
    #         print(row)
    return render(request, 'UserApp/details.html')

def contact(request):
    return render(request, 'UserApp/contact.html')

def signin_admin(request):
    # if request.method == "POST":
    #     data = request.POST
    #     if len(data) == 4:
    #         with connection.cursor() as cursor:
    #             cursor.execute("SELECT * FROM ADMINISTRATORS WHERE AEMAIL = %s AND APASSWORD = %s AND APASSCODE = %s", [request.POST.get('email'), request.POST.get('password'), request.POST.get('passcode')])
    #             row = cursor.fetchall()
    #             print(row)
            #     if row:
            #         return render(request, 'UserApp/admin.html')
            #     else:
            #         return render(request, 'UserApp/signin_admin.html')
    return render(request, 'UserApp/signin_admin.html')