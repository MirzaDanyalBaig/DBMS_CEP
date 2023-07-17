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
        if len(data) == 3:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM CUSTOMERS WHERE CEMAIL = %s AND CPASSWORD = %s", [request.POST.get('email'), request.POST.get('password')])
                row = cursor.fetchone()
                id, *_ = row
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

def products(request, context):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        context1 = {'products': products,}
    return render(request, 'UserApp/products.html', context=context1)

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
    if request.method == "POST":
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM PRODUCTS WHERE PRODID = %s", [request.POST.get('product_id')])
            row = cursor.fetchone()
            cursor.execute("SELECT * FROM ELECTRONICS WHERE PRODID = %s", [request.POST.get('product_id')])
            row_2 = cursor.fetchone()
            cursor.close()
            connection.close()
            if row:
                if row[3] == 0 or row[3] == None or row[3] == "0" or row[3] == "None" or row[3] == "NULL":
                    avail = "Out of Stock"
                else:
                    avail = "In Stock"
                return render(request, 'UserApp/details.html', context={'available': avail, 'product': row, 'product_2': row_2})
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
        customer_id = 1
        cursor.execute("SELECT * FROM customers WHERE CustID = %s", [customer_id])
        customers = cursor.fetchall()
        print(customer_id, customers)
        context = {'customers': customers,}
    return render(request, 'UserApp/profile_customer.html', context=context)

def details_manager(request):
    with connection.cursor() as cursor:
        cursor.execute("Select a.AdminID, a.AName, a.AEmail, a.APassword, a.PassCode, j.JobType, j.Salary from administrators a, job j Where a.PassCode = j.PassCode and a.PassCode <> 1;")
        details = cursor.fetchall()
        context = {'details': details,}
    return render(request, 'UserApp/details_manager.html', context=context)

def details_supervisor(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM customers;")
        details = cursor.fetchall()
        context = {'details': details,}
    return render(request, 'UserApp/details_supervisor.html', context=context)

def details_stockclerk(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM products;")
        details = cursor.fetchall()
        context = {'details': details,}
    return render(request, 'UserApp/details_stockclerk.html', context=context)

def shopping_history(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM order;")
        details = cursor.fetchall()
        context = {'details': details,}
    return render(request, 'UserApp/shopping_history.html', context=context)
    

def profile_admin(request):
    with connection.cursor() as cursor:
        cursor.execute("Select a.AName, a.AEmail, a.APassword, a.PassCode, j.JobType, j.Salary from administrators a, job j Where a.PassCode = j.PassCode;")
        customers = cursor.fetchall()
        context = {'customers': customers,}
    return render(request, 'UserApp/profile_admin.html', context=context)
