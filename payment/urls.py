# dj_razorpay/urls.py

from django.contrib import admin
from django.urls import path
from payment import views

urlpatterns = [
	path('payment/', views.homepage, name='index-payment'),
	path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
]
