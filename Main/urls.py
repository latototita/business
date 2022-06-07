from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = 'Main'

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contact'),
    path('services', services, name='services'),
    path('about', about, name='about'),
]