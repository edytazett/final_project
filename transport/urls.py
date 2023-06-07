"""
URL configuration for final_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from transport import views

urlpatterns = [
    path('', views.MainPageView.as_view(), name='main_page'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('my_company', views.MyCompanyView.as_view(), name='my_company'),
    path('exports/', views.ExportsView.as_view(), name='exports'),
    path('imports/', views.ImportsView.as_view(), name='imports'),
    path('customer_create/', views.CustomerCreateView.as_view(), name='customer_create'),
    path('customer_update/<int:pk>/', views.CustomerUpdateView.as_view(), name='customer_update'),
    path('customer_list/', views.CustomerListView.as_view(), name='customer_list'),
    path('person_create/', views.PersonCreateView.as_view(), name='person_create'),
    path('person_update/<int:pk>/', views.PersonUpdateView.as_view(), name='person_update'),
    path('employee_create/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('employee_update/<int:pk>/', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('order_create/', views.OrderCreateView.as_view(), name='order_create'),
    path('order_update/<int:pk>/', views.OrderUpdateView.as_view(), name='order_update'),
    path('order_list/', views.OrderListView.as_view(), name='order_list'),
    path('truck_create/', views.TruckCreateView.as_view(), name='truck_create'),
    path('truck_update/', views.TruckUpdateView.as_view(), name='truck_update'),
    path('trailer_create/', views.TrailerCreateView.as_view(), name='trailer_create'),
    path('trailer_update/', views.TrailerUpdateView.as_view(), name='trailer_update'),


]
