"""
URL configuration for alphaVantage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from stockVisualizer import views #NEW FROM CHAT TO FIX ERROR WHICH OCCURE WHEN RUNNING THE WEBSITE IN MY LOCOAL ENVIRONMENT 
import stockVisualizer.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", stockVisualizer.views.home), # makes sure the when usere visits the home page; html (web browser), the backend; views.py is called 
    path('get_stock_data/', stockVisualizer.views.get_stock_data), #makes sure the get_stock_data function in views.py is called when home.html makes an AJAX POST request to the /get_stock_data/ URL.
]                                                                   # ^URL ROUTING 
