from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.db import connection
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def index(request):
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'UserApp/index.html')

def signin(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        if len(data) == 3:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM CUSTOMERS WHERE CEMAIL = %s AND CPASSWORD = %s", [request.POST.get('email'), request.POST.get('password')])
                row = cursor.fetchone()
                print(row)
                cursor.close()
                connection.close()
                if row:
                    return redirect('products')
                else:
                    # Display an error message and redirect to the same page
                    messages.error(request, 'Invalid Credentials.')
                    return redirect(reverse('signin'))
                
        elif len(data) == 7:
            if request.POST.get('password') == request.POST.get('password_2'):
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM CUSTOMERS WHERE CEMAIL = %s", [request.POST.get('email')])
                    row = cursor.fetchone()
                    cursor.close()
                    connection.close()
                    if row:
                        messages.error(request, 'Account Already Exists.')
                        return redirect(reverse('signin'))
                    else:
                        with connection.cursor() as cursor:
                            cursor.execute("INSERT INTO CUSTOMERS(CNAME, CEMAIL, CCOUNTRY, CCITY, CPASSWORD) VALUES(%s, %s, %s, %s, %s)", [request.POST.get('name'), request.POST.get('email'), request.POST.get('country'), request.POST.get('city'), request.POST.get('password')])
                            cursor.close()
                            connection.close()
                            messages.error(request, 'Account Created Successfully.')
                            return redirect(reverse('signin'))
                
            else:
                # Display an error message and redirect to the same page
                messages.error(request, 'Passwords Do Not Match.')
                return redirect(reverse('signin'))
        else:
            return render(request, 'UserApp/signin.html')
    # Render the HTML template signin.html with the data in the context variable
    return render(request, 'UserApp/signin.html')

def manager_admin(request):
    # Render the HTML template admin.html with the data in the context variable
    return render(request, 'UserApp/manager_admin.html')

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
    if request.method == "GET":
    #     with connection.cursor() as cursor:
    #         cursor.execute("SELECT * FROM product where product_id = {}", [request.GET.get('product_id')])
    #         row = cursor.fetchall()
    #         print(row)
    return render(request, 'UserApp/details.html')

def contact(request):
    return render(request, 'UserApp/contact.html')

def signin_admin(request):
    if request.method == "POST":
        data = request.POST
        
        if len(data) == 4:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM ADMINISTRATORS WHERE AEMAIL = %s AND APASSWORD = %s AND PASSCODE = %s", [request.POST.get('email'), request.POST.get('password'), request.POST.get('passcode')])
                row = cursor.fetchone()
                cursor.close()
                connection.close()
                print(row)
                if row:
                    return redirect('admin')
                else:
                    # Display an error message and redirect to the same page
                    messages.error(request, 'Invalid Credentials.')
                    return redirect(reverse('signin_admin'))
                
        elif len(data) == 7:
            if request.POST.get('password') == request.POST.get('password_2'):
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM ADMINISTRATORS WHERE AEMAIL = %s", [request.POST.get('email')])
                    row = cursor.fetchone()
                    cursor.close()
                    connection.close()
                    if row:
                        messages.error(request, 'Account Already Exists.')
                        return redirect(reverse('signin_admin'))
                    else:
                        with connection.cursor() as cursor:
                            cursor.execute("INSERT INTO ADMINISTRATORS(ANAME, AEMAIL, AJOB, PASSCODE, APASSWORD) VALUES(%s, %s, %s, %s, %s)", [request.POST.get('name'), request.POST.get('email'), request.POST.get('job'), request.POST.get('passcode'), request.POST.get('password')])
                            cursor.close()
                            connection.close()
                            messages.error(request, 'Account Created Successfully.')
                            return redirect(reverse('signin_admin'))
                
            else:
                # Display an error message and redirect to the same page
                messages.error(request, 'Passwords Do Not Match.')
                return redirect(reverse('signin_admin'))
        else:
            return render(request, 'UserApp/signin_admin.html')
    return render(request, 'UserApp/signin_admin.html')


def profile_customer(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM customers")
        customers = cursor.fetchall()
        # print(products)
        context = {'customers': customers,}
    return render(request, 'UserApp/profile_customer.html', context=context)