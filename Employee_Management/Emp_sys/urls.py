"""
URL configuration for Employee_Management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('payments/', views.payments, name='payments'),
    path('actions_payments/', views.actions_payments, name='actions_payments'),
    path('actions_employee/', views.actions_employee, name='actions_employee'),
    path('history/', views.history, name='history'),
    path('delete_employee/<str:matricule>/', views.delete_employee, name='delete_employee'),
    path('delete_payment/<str:matricule>/', views.delete_payment, name='delete_payment'),


]
