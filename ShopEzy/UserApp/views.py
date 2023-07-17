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
    # Check if the request method is POST
    if request.method == "POST":
        # Get the data from the POST request
        data = request.POST
        # Check if the data has 3 elements
        if len(data) == 3:
            # Connect to the database using the cursor
            with connection.cursor() as cursor:
                # Execute the query
                cursor.execute("SELECT * FROM CUSTOMERS WHERE CEMAIL = %s AND CPASSWORD = %s", [request.POST.get('email'), request.POST.get('password')])
                # Fetch the first row
                row = cursor.fetchone()
                id, *_ = row
                # Close the cursor
                cursor.close()
                # Close the connection
                connection.close()
                # Check if the row exists
                if row:
                    # Redirect to the products page
                    return redirect('products')
                # If the row does not exist
                else:
                    # Display an error message error
                    messages.error(request, 'Invalid Credentials.')
                    # Redirect to the signin page
                    return redirect(reverse('signin'))
        
        # Check if the data has 7 elements
        elif len(data) == 7:
            # Check if the password and confirm password match
            if request.POST.get('password') == request.POST.get('password_2'):
                # Connect to the database using the cursor
                with connection.cursor() as cursor:
                    # Execute the query
                    cursor.execute("SELECT * FROM CUSTOMERS WHERE CEMAIL = %s", [request.POST.get('email')])
                    # Fetch the first row
                    row = cursor.fetchone()
                    # Close the cursor
                    cursor.close()
                    # Close the connection
                    connection.close()
                    # Check if the row exists
                    if row:
                        # Display an error message error
                        messages.error(request, 'Account Already Exists.')
                        # Redirect to the signin page
                        return redirect(reverse('signin'))
                    # If the row does not exist
                    else:
                        # Connect to the database using the cursor
                        with connection.cursor() as cursor:
                            # Execute the query
                            cursor.execute("INSERT INTO CUSTOMERS(CNAME, CEMAIL, CCOUNTRY, CCITY, CPASSWORD) VALUES(%s, %s, %s, %s, %s)", [request.POST.get('name'), request.POST.get('email'), request.POST.get('country'), request.POST.get('city'), request.POST.get('password')])
                            # Close the cursor
                            cursor.close()
                            # Close the connection
                            connection.close()
                            # Display an error message error
                            messages.error(request, 'Account Created Successfully.')
                            # Redirect to the signin page
                            return redirect(reverse('signin'))
            # If the password and confirm password do not match    
            else:
                # Display an error message error
                messages.error(request, 'Passwords Do Not Match.')
                # Redirect to the signin page
                return redirect(reverse('signin'))
        # If the data has neither 3 nor 7 elements
        else:
            # Render the HTML template signin.html
            return render(request, 'UserApp/signin.html')
    # Render the HTML template signin.html
    return render(request, 'UserApp/signin.html')

def manager_admin(request):
    # Render the HTML template admin.html
    return render(request, 'UserApp/manager_admin.html')

def products(request):
    # Connect to the database using the cursor
    with connection.cursor() as cursor:
        # Execute the query
        cursor.execute("SELECT * FROM PRODUCTS P, ELECTRONICS E WHERE P.PRODID=E.PRODID")
        # Fetch all the rows
        products = cursor.fetchall()
        # Store the rows in the context variable
        context = {'products': products,}
    # Render the HTML template products.html with the data in the context variable
    return render(request, 'UserApp/products.html', context=context)

def products_garments(request):
    # Render the HTML template products_garments.html
    return render(request, 'UserApp/products_garments.html')

def products_groceries(request):
    # Render the HTML template products_groceries.html
    return render(request, 'UserApp/products_groceries.html')

def cart(request):
    # Render the HTML template cart.html
    return render(request, 'UserApp/cart.html')

def checkout(request):
    # Render the HTML template checkout.html
    return render(request, 'UserApp/checkout.html')

def details(request):
    # Check if the request method is POST
    if request.method == "POST":
        # Connect to the database using the cursor
        with connection.cursor() as cursor:
            # Execute the query
            cursor.execute("SELECT * FROM PRODUCTS WHERE PRODID = %s", [request.POST.get('product_id')])
            # Fetch the first row
            row = cursor.fetchone()
            # Execute the query
            cursor.execute("SELECT * FROM ELECTRONICS WHERE PRODID = %s", [request.POST.get('product_id')])
            # Fetch the first row
            row_2 = cursor.fetchone()
            # Close the cursor
            cursor.close()
            # Close the connection
            connection.close()
            # Check if the row exists
            if row:
                # Check if the value of the 4th column is 0 or None or "0" or "None" or "NULL"
                if row[3] == 0 or row[3] == None or row[3] == "0" or row[3] == "None" or row[3] == "NULL":
                    # Set the value of avail to "Out of Stock"
                    avail = "Out of Stock"
                # If the value of the 4th column is not 0 or None or "0" or "None" or "NULL"
                else:
                    # Set the value of avail to "In Stock"
                    avail = "In Stock"
                # Render the HTML template details.html with the data in the context variable
                return render(request, 'UserApp/details.html', context={'available': avail, 'product': row, 'product_2': row_2})
    # Render the HTML template details.html
    return render(request, 'UserApp/details.html')

def details_garments(request):
    # Check if the request method is POST
    if request.method == "POST":
        # Connect to the database using the cursor
        with connection.cursor() as cursor:
            # Execute the query
            cursor.execute("SELECT * FROM PRODUCTS WHERE PRODID = %s", [request.POST.get('product_id')])
            # Fetch the first row
            row = cursor.fetchone()
            # Execute the query
            cursor.execute("SELECT * FROM GARMENTS WHERE PRODID = %s", [request.POST.get('product_id')])
            # Fetch the first row
            row_2 = cursor.fetchone()
            # Close the cursor
            cursor.close()
            # Close the connection
            connection.close()
            # Check if the row exists
            if row:
                # Check if the value of the 4th column is 0 or None or "0" or "None" or "NULL"
                if row[3] == 0 or row[3] == None or row[3] == "0" or row[3] == "None" or row[3] == "NULL":
                    # Set the value of avail to "Out of Stock"
                    avail = "Out of Stock"
                # If the value of the 4th column is not 0 or None or "0" or "None" or "NULL"
                else:
                    # Set the value of avail to "In Stock"
                    avail = "In Stock"
                # Render the HTML template details_garments.html with the data in the context variable
                return render(request, 'UserApp/details_garments.html', context={'available': avail, 'product': row, 'product_2': row_2})
    # Render the HTML template details_garments.html
    return render(request, 'UserApp/details_garments.html')

def details_groceries(request):
    # Check if the request method is POST
    if request.method == "POST":
        # Connect to the database using the cursor
        with connection.cursor() as cursor:
            # Execute the query
            cursor.execute("SELECT * FROM PRODUCTS WHERE PRODID = %s", [request.POST.get('product_id')])
            # Fetch the first row
            row = cursor.fetchone()
            # Execute the query
            cursor.execute("SELECT * FROM GROCERIES WHERE PRODID = %s", [request.POST.get('product_id')])
            # Fetch the first row
            row_2 = cursor.fetchone()
            # Close the cursor
            cursor.close()
            # Close the connection
            connection.close()
            # Check if the row exists
            if row:
                # Check if the value of the 4th column is 0 or None or "0" or "None" or "NULL"
                if row[3] == 0 or row[3] == None or row[3] == "0" or row[3] == "None" or row[3] == "NULL":
                    # Set the value of avail to "Out of Stock"
                    avail = "Out of Stock"
                # If the value of the 4th column is not 0 or None or "0" or "None" or "NULL"
                else:
                    # Set the value of avail to "In Stock"
                    avail = "In Stock"
                # Render the HTML template details_groceries.html with the data in the context variable
                return render(request, 'UserApp/details_groceries.html', context={'available': avail, 'product': row, 'product_2': row_2})
    # Render the HTML template details_groceries.html
    return render(request, 'UserApp/details_groceries.html')

def contact(request):
    # Render the HTML template contact.html
    return render(request, 'UserApp/contact.html')

def signin_admin(request):
    # Check if the request method is POST
    if request.method == "POST":
        # Get the data from the POST request
        data = request.POST
        # Check if the data has 4 elements
        if len(data) == 4:
            # Connect to the database using the cursor
            with connection.cursor() as cursor:
                # Execute the query
                cursor.execute("SELECT * FROM ADMINISTRATORS WHERE AEMAIL = %s AND APASSWORD = %s AND PASSCODE = %s", [request.POST.get('email'), request.POST.get('password'), request.POST.get('passcode')])
                # Fetch the first row
                row = cursor.fetchone()
                # Close the cursor
                cursor.close()
                # Close the connection
                connection.close()
                # Check if the row exists
                if row:
                    # Redirect to the admin page
                    return redirect('admin')
                else:
                    # Display an error message error
                    messages.error(request, 'Invalid Credentials.')
                    # Redirect to the signin_admin page
                    return redirect(reverse('signin_admin'))
                
        # Check if the data has 7 elements
        elif len(data) == 7:
            # Check if the password and confirm password match
            if request.POST.get('password') == request.POST.get('password_2'):
                # Connect to the database using the cursor
                with connection.cursor() as cursor:
                    # Execute the query
                    cursor.execute("SELECT * FROM ADMINISTRATORS WHERE AEMAIL = %s", [request.POST.get('email')])
                    # Fetch the first row
                    row = cursor.fetchone()
                    # Close the cursor
                    cursor.close()
                    # Close the connection
                    connection.close()
                    # Check if the row exists
                    if row:
                        # Display an error message error
                        messages.error(request, 'Account Already Exists.')
                        # Redirect to the signin_admin page
                        return redirect(reverse('signin_admin'))
                    # If the row does not exist
                    else:
                        # Connect to the database using the cursor
                        with connection.cursor() as cursor:
                            # Execute the query
                            cursor.execute("INSERT INTO ADMINISTRATORS(ANAME, AEMAIL, AJOB, PASSCODE, APASSWORD) VALUES(%s, %s, %s, %s, %s)", [request.POST.get('name'), request.POST.get('email'), request.POST.get('job'), request.POST.get('passcode'), request.POST.get('password')])
                            # Close the cursor
                            cursor.close()
                            # Close the connection
                            connection.close()
                            # Display an error message error
                            messages.error(request, 'Account Created Successfully.')
                            # Redirect to the signin_admin page
                            return redirect(reverse('signin_admin'))
            # If the password and confirm password do not match
            else:
                # Display an error message error
                messages.error(request, 'Passwords Do Not Match.')
                # Redirect to the signin_admin page
                return redirect(reverse('signin_admin'))
        # If the data has neither 4 nor 7 elements
        else:
            # Render the HTML template signin_admin.html
            return render(request, 'UserApp/signin_admin.html')
    # Render the HTML template signin_admin.html
    return render(request, 'UserApp/signin_admin.html')


def profile_customer(request):
    # Connect to the database using the cursor
    with connection.cursor() as cursor:
        # Execute the query
        cursor.execute("SELECT * FROM customers")
        # Fetch all the rows
        customers = cursor.fetchall()
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
