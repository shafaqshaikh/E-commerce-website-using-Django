from django.contrib import admin
from django.urls import path
from . import views
from .forms import ModelForm

urlpatterns = [
    path('' , views.home , name='home'),
    path('products/' , views.products , name='products'),
    path('customer/<str:pk>/' , views.customer , name='customer'),
    path('create_order/<str:pk>' ,views.createOrder , name='create_order'),
    #path('update_order/<str:pk>' , views.updateOrder , name='update_order'),
    #path('delete_order/<str:pk>' , views.deleteOrder , name='delete_order'),
    path('register' , views.register , name='register'),
    path('login' , views.loginpage , name='login'),
    path('logout' , views.logoutpage , name='logout'),
]


