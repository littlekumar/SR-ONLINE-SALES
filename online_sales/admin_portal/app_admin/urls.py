"""admin_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.views.generic import TemplateView,View

from app_admin import views

urlpatterns = [

    path('home/',TemplateView.as_view(template_name="index.html"),name="home"),
    path('index/',TemplateView.as_view(template_name="admin_login.html"),name="admin_login"),
    path('admin_login_verification/',views.admin_Login_Verification,name="admin_login_verification"),
    path('admin_home_button_action/',views.admin_home_button_action,name="admin_home_button_action"),
    path('merchant/',TemplateView.as_view(template_name="merchant.html"),name="merchant"),
    path('sales/',TemplateView.as_view(template_name="sales.html"),name="sales"),
    path('complaint/',TemplateView.as_view(template_name="complaint.html"),name="complaint"),
    path('merchant_actions/',views.merchant_actions,name="merchant_actions"),
    path('save_merchant/',views.save_merchant,name="save_merchant"),
    path('login_merchant/',views.Login_merchant.as_view(),name="login_merchant"),
    path('change_merchant_password/',views.Change_merchant_password.as_view(),name="change_merchant_password"),
    path('update_merchant_password/',views.Update_merchant_password.as_view(),name="update_merchant_password"),
    path('add_product/',views.Add_product.as_view(),name="add_product"),
    path('product_update/',views.Product_update.as_view(),name="product_update"),
    path('delete_product/',views.Delete_product.as_view(),name="delete_product"),
    path('update_product_data/',views.Update_product_data.as_view(),name="update_product_data"),

]
