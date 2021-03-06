"""hccopy URL Configuration

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
from . import views as auth_view

urlpatterns = [
    # path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', auth_view.Logout.as_view(), name='logout'),
    # path('password_change/', auth_view.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    # path('password_change_done/', auth_view.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    # path('user_register/', user_register_page, name='register'),
    # path('user_register_idcheck', user_register_idcheck, name='registeridcheck'),
    # path('user_register_res/', user_register_result, name='registerres'),
    # path('user_register_completed/', user_register_completed, name='registercompleted'),
]