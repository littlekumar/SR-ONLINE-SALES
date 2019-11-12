"""online_sales_merchant URL Configuration

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
from django.views.generic import TemplateView

from online_merchant_sales import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name="index_merchant.html"),name="home"),
    path('merchant_login_page/',TemplateView.as_view(template_name="merchant_login_page.html"),name="merchant_login_page"),
    path('login_merchant/',views.login_merchant,name="login_merchant"),
    path('get_email/',TemplateView.as_view(template_name="email_verification.html"),name="get_email"),
    path('change_password/',views.change_password,name="change_password"),
    path('update_password/',views.update_password,name="update_password"),
    path('merchant_home_button_actions/',views.merchant_home_button_actions,name="merchant_home_button_actions"),
    path('addproducts/',views.addproducts,name="addproducts"),
    path('update_product/',views.update_product,name="update_product"),
    path('delete_product/',views.delete_product,name="delete_product"),
    path('button_action/',views.button_action,name="button_action")
]
