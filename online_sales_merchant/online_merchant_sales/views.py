import requests
from django.core.serializers import serialize
from django.shortcuts import render,redirect
from online_merchant_sales.merchant_login import merchant_login_verification
import json

# Create your views here.
def login_merchant(request):
    email = request.POST.get("username")
    password = request.POST.get("pass")

    data = {
        "email":email,
        "password":password
    }

    json_Data = json.dumps(data)

    res = requests.post("http://127.0.0.1:3000/login_merchant/",json_Data)



    code = res.status_code

    if code == 200:
        return render(request,"merchant_home.html")
    else:
        return render(request,"merchant_login_page.html",{"message":"You Entered Wrong Details"})


def change_password(request):
    email = request.POST.get("email")
    json_data = json.dumps(email)
    res = requests.post("http://127.0.0.1:3000/change_merchant_password/", json_data)
    code = res.status_code
    json_data_res = res.json()
    print(json_data_res)



    if code == 200:
        return render(request,"password_update.html",{"data":json_data_res})
    else:
        return render(request,"home.html",{"message":"You Entered Wrong Details"})


def update_password(request):
    merchant_id = request.POST.get("merchant_id")
    merchant_name = request.POST.get("merchant_name")
    merchant_contact = request.POST.get("merchant_contact")
    merchant_email = request.POST.get("merchant_email")
    merchant_password = request.POST.get("merchant_password")
    merchant_new_password = request.POST.get("merchant_new_password")
    merchant_retype_new_password = request.POST.get("merchant_retype_new_password")

    print(merchant_retype_new_password)

    data = {
        "merchant_id":merchant_id,"merchant_name":merchant_name,"merchant_contact":merchant_contact,"merchant_email":merchant_email,
        "merchant_password":merchant_password,"merchant_retype_new_password":merchant_retype_new_password,"merchant_new_password":merchant_new_password
    }

    json_data = json.dumps(data)

    res = requests.post("http://127.0.0.1:3000/update_merchant_password/", json_data)

    code = res.status_code


    if code == 200:
        return render(request, "merchant_login_page.html", {"message": "password changed successfully"})
    else:
        return render(request, "merchant_login_page.html", {"message": "You Entered Wrong Details"})

def merchant_home_button_actions(request):
    button = request.POST.get("btn")

    if button == "product":
        return render(request, "product.html")
    if button == "sales":
        return render(request, "sales.html")
    if button == "customers":

        return render(request, "customers.html")
    if button == "complaints":
        return render(request, "complaints.html")
    if button == "logout":
        return render(request, "index_merchant.html")


def addproducts(request):
    product_no = request.POST.get("product_no")
    product_name = request.POST.get("product_name")
    price = request.POST.get("price")
    quantity = request.POST.get("quantity")
    merchant_id = request.POST.get("merchant_id")

    product = {
        "product_no":product_no,"product_name":product_name,"price":price,"quantity":quantity,"merchant_id":merchant_id
    }

    json_data = json.dumps(product)
    print(json_data)

    result = requests.post("http://127.0.0.1:3000/add_product/", json_data)

    data= result.json()

    code = result.status_code


    if code == 200:
        return render(request, "product.html",{"data":data})
    else:
        return render(request, "product.html", {"message": "You Entered Wrong Details"})


def update_product(request):
    data = request.GET.get("id")
    product_id = data
    result = requests.post("http://127.0.0.1:3000/product_update/", product_id)

    data = result.json()
    print(data)


    return render(request, "product.html",{"product_data":data})


def delete_product(request):
    data = request.GET.get("id")
    product_id = data

    result = requests.post("http://127.0.0.1:3000/delete_product/", product_id)
    data = result.json()

    return render(request, "product.html",{"data":data})


def button_action(request):
    button = request.POST.get("btn")
    print(button)

    if button == "save":
        return addproducts(request)
    if button == "update":
        return update_product_data(request)

def update_product_data(request):

    product_no = request.POST.get("product_no")
    product_name = request.POST.get("product_name")
    price = request.POST.get("price")
    quantity = request.POST.get("quantity")

    data = {
        "product_no": product_no, "product_name": product_name, "price": price,
        "quantity": quantity,

    }

    json_data = json.dumps(data)

    res = requests.post("http://127.0.0.1:3000/update_product_data/", json_data)

    data = res.json()

    return render(request, "product.html",{"data":data})




