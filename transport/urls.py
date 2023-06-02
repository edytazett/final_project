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
    path('client_create/', views.ClientCreateView.as_view(), name='client_create'),
    path('client_update/<int:pk>/', views.ClientUpdateView.as_view(), name='client_update'),
    path('client_list/', views.ClientListView.as_view(), name='client_list'),
    path('person_create/', views.PersonCreateView.as_view(), name='person_create'),
    path('person_update/<int:pk>/', views.PersonUpdateView.as_view(), name='person_update'),
    path('employee_create/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('employee_update/<int:pk>/', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('order_create/', views.OrderCreateView.as_view(), name='order_create'),
    path('order_update/<int:pk>/', views.OrderUpdateView.as_view(), name='order_update'),
    path('order_list/', views.OrderListView.as_view(), name='order_list')

]
