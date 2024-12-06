from django.shortcuts import render, redirect

from book.form import UserRegistrationForm
from django.contrib.auth.models import User

from .models import Product

from restframework.view import APIView


def register_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Process the form data
            User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            return redirect('success_page')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form}) 



"""	•	Requirements:
	•	Create a view that fetches all products with prices below a value passed in the query parameter (?max_price=100).
	•	Render the filtered products on a template.
	•	Handle cases where no products match the criteria."""
 
 
 
# class ProductListView(APIView):
#     def get(self, request):
#         max_price = request.query_params.get('max_price')
#         if max_price:
#             products = Product.objects.filter(price__lt=max_price)
#         else:
#             products = Product.objects.all()
#         return Response(products)


def product_list(request):
    max_price = request.GET.get('max_price')
    if max_price:
        products = Product.objects.filter(price__lt=max_price)
    else:
        products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})




"""
Task: Create a simple Django view that counts how many times a user has visited a page.
	•	Requirements:
	•	Use Django’s session framework to store the count.
	•	Increment the counter on each visit.
	•	Display the count on a simple HTML template.
	•	Expected Output: A page showing You have visited this page X times.
"""


def page_visit_count(request):
    visit_amount = request.session.get('visit_amount', 0)
    visit_amount += 1
    request.session['visit_amount'] = visit_amount
    
    return render(request, 'visit_count.html', {'visit_amount': visit_amount})