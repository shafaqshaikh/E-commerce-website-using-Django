from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login , logout
from .models import *
from .forms import OrderForm , CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user , allowed_user
@login_required(login_url='login')
@allowed_user(allowed_user=['admins'])
def home(request):
	orders=Order.objects.all()
	customers=Customer.objects.all()
	total_customers=customers.count()
	total_orders=orders.count()
	delivered=orders.filter(status='delivered').count()
	pending=orders.filter(status='pending').count()
	context={'orders':orders , 'customer':customers , 'total_customers':total_customers , 'total_orders':total_orders , 'delivered':delivered , 'pending':pending}
	return render(request , 'accounts/dashboard.html'  , context)
@allowed_user(allowed_user=['admins'])
def products(request):
	products=Products.objects.all()
	return render(request , 'accounts/products.html' , {'products': products})
@allowed_user(allowed_user=['admins'])
def customer(request , pk):
	customer=Customer.objects.get(id=pk)
	orders=customer.order_set.all()
	context={'customer':customer , 'orders':orders}
	return render(request , 'accounts/customer.html' , context)
@allowed_user(allowed_user=['admins'])
def createOrder(request , pk):
	customer=Customer.objects.get(id=pk)
	form= OrderForm()
	if request.method=='POST':
		form= OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context={'form':form , 'customer':customer}
	return render(request , 'accounts/orderform.html' , context)

#def updateOrder(request):

#def deleteOrder(request):


def register(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:

		form=CreateUserForm()
		if request.method=='POST':
			form=CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user=form.cleaned_data.get('username')
				messages.success(request , 'Account is created for ' + user)
				return redirect('login')


		context={'form':form}
		return render(request , 'accounts/register.html' , context)

@unauthenticated_user
def loginpage(request):
	
		if request.method=='POST':
			username=request.POST.get('username')
			password=request.POST.get('password')
			user=authenticate(request , username=username , password=password)
			if user is not None:
				login(request , user)
				return redirect('home')
			else:
				messages.info(request , 'Username or Password is incorrect')
		context={}
		return render(request , 'accounts/login.html' , context)

def logoutpage(request):
	logout(request)
	return redirect('login')