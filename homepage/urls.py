"""hc_print_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from . import views
# customer, product, index, introduce, notice

urlpatterns = [
    path('', views.home, name="home"),
    path('default/', views.blog_to_home),
    path('prod_list/<str:product_name>/', views.product_view, name='product_detail'),
    path('product/', views.product, name="product"),
    path('introduce/', views.introduce, name="introduce"),
    path('notice/', views.notice, name="notice"),
    path('customer/', views.customer, name="customer"), 
    path('index/', views.index, name="index"),
    path('init/', views.initial,),
    path('init_list/', views.initial_list,),
    path('del/', views.delete_init,),
    path('contact/sent/', views.transfer_to_email, name='to_email'),
]
