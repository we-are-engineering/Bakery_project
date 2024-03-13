"""
URL configuration for Cake_Shop project.

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
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name='homepage'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('add_customer/', views.add_customer, name='add-customer'),
    path('add_item/', views.add_item, name='add-item'),
    path('add_product/', views.add_product,name='add-product'),
    path('add-supplier/' , views.add_supplier, name='add-supplier'),
    path('add_supplierorder/',views.add_supplyorder, name='add-supply-order'),
    path('conform_order/', views.conform_order, name='conform-order'),
    path('find_customer/', views.find_customer, name='find-customer'),
    path('view_order/', views.view_order, name='view-order'),
    path('view_homedelivery/',views.view_delivery, name='view-home-delivery'),
    path('dashboard/', views.dashboard,name='dashboard')
]
