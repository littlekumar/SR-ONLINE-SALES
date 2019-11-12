from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.crypto import random
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import MerchantModel,ProductModel
import json
from django.views.generic import View


def admin_Login_Verification(request):
    email = request.POST.get("email")
    print(email)
    password = request.POST.get("pass")
    print(password)
    if email == "admin@gmail.com" and password == "admin":
        return render(request, "admin_welcome_page.html")
    else:
        return render(request, "admin_login.html", {"message": "Wrong Entry"})


def admin_home_button_action(request):
    button_action = request.POST.get("btn")
    print(button_action)

    if button_action == "merchant":
        return render(request,"merchant.html")
    if button_action == "sales":
        return render(request,"sales.html")
    if button_action == "complaint":
        return render(request,"complaint.html")
    if button_action == "logout":
        return render(request,"index.html")


def merchant_actions(request):
    button = request.POST.get("btn")

    if button == "add_merchant":
        return render(request,"add_merchant.html")
    if button == "view_merchant":
        data = MerchantModel.objects.all()
        return render(request,"view_merchant.html",{"data":data})
    if button == "update_merchant":
        return render(request,"update_merchant.html")
    if button == "delete_merchant":
        return render(request,"delete_merchant.html")
    if button == "logout":
        return render(request,"index.html")

def gen_idno():
    qs = MerchantModel.objects.all()
    if qs:
        return qs[len(qs)-1].Merchant_Id+1

    else:
        return 101



def save_merchant(request):
    Name = request.POST.get("name")
    CONTACT = request.POST.get("contact")
    EMAIL = request.POST.get("email")
    Password = random.randint(10000000,99999999)
    IdNo = gen_idno()


    MerchantModel(Merchant_Name=Name,Merchant_Contact=CONTACT,Merchant_Email=EMAIL,Merchant_Password=Password,Merchant_Id=IdNo).save()

    return render(request,"merchant.html",{"message":"merchant saved successfully"})

# def login_merchant(request):
#
#         data = request.body
#         print(data)

@method_decorator(csrf_exempt,name="dispatch")
class Login_merchant(View):
    def post(self,request,*args,**kwargs):
        json_dat = json.loads(request.body)

        email = json_dat['email']
        password = json_dat['password']

        try:
             data=MerchantModel.objects.get(Merchant_Email=email,Merchant_Password=password)

             dict_type_data = {"Merchant_Id":data.Merchant_Id,"Merchant_Name":data.Merchant_Name,"Merchant_Contact":data.Merchant_Contact,"Merchant_Email":data.Merchant_Email,"Merchant_Password":data.Merchant_Password}

             json_data = json.dumps(dict_type_data)

             return HttpResponse(json_data,content_type='application/json', status=200)
             # return HttpResponse(data, content_type="application/json", status=200)

        except:
            # json_data=json.dumps({'error':"Invalid UserId or Password"})
            return HttpResponse(content_type="application/json", status=400)
            # return HttpResponse(content_type="application/json", status=400)

@method_decorator(csrf_exempt,name="dispatch")
class Change_merchant_password(View):
    def post(self,request,*args,**kwargs):
        json_dat = json.loads(request.body)
        email = json_dat
        print(email)


        try:
             data=MerchantModel.objects.get(Merchant_Email=email)
             print(data.Merchant_Name)

             dict_type_data = {"Merchant_Id": data.Merchant_Id, "Merchant_Name": data.Merchant_Name,
                               "Merchant_Contact": data.Merchant_Contact, "Merchant_Email": data.Merchant_Email,
                               "Merchant_Password": data.Merchant_Password}
             json_data = json.dumps(dict_type_data)

             return HttpResponse(json_data,content_type='application/json', status=200)
             # return HttpResponse(data, content_type="application/json", status=200)

        except:
            # json_data=json.dumps({'error':"Invalid UserId or Password"})
            return HttpResponse(content_type="application/json", status=400)
            # return HttpResponse(content_type="application/json", status=400)

@method_decorator(csrf_exempt,name="dispatch")
class Update_merchant_password(View):
    def post(self,request):
        data = json.loads(request.body)
        merchant_id = data['merchant_id']
        merchant_name = data['merchant_name']
        merchant_contact = data['merchant_contact']
        merchant_email = data['merchant_email']
        merchant_password = data['merchant_password']
        merchant_new_password = data['merchant_new_password']
        merchant_retype_new_password = data['merchant_retype_new_password']

        try:
            if merchant_new_password == merchant_retype_new_password:
                MerchantModel.objects.filter(Merchant_Email=merchant_email).update(Merchant_Password=merchant_new_password)
                return HttpResponse(content_type='application/json', status=200)
        except:

            return HttpResponse(content_type="application/json", status=400)

@method_decorator(csrf_exempt,name="dispatch")
class Add_product(View):
    def post(self,request):
        data = json.loads(request.body)

        product_no = data['product_no']
        product_name = data['product_name']
        price = data['price']
        quantity = data['quantity']
        merchant_id = data['merchant_id']

        print(product_name)
        print(product_no)

        try:

            ProductModel(PRODUCT_NO=product_no,PRODUCT_NAME=product_name,PRODUCT_PRICE=price,PRODUCT_QUANTITY=quantity,Merchant_Id_id=merchant_id).save()
            print("try1")


        except:
            return HttpResponse(content_type="application/json", status=400)

        finally:
            products_Data = ProductModel.objects.all()
            json_data = serialize("json", products_Data, fields=("PRODUCT_NO", "PRODUCT_NAME", "PRODUCT_PRICE","PRODUCT_QUANTITY"))

            print(json_data)

            return HttpResponse(json_data, content_type='application/json')

@method_decorator(csrf_exempt,name="dispatch")
class Product_update(View):

    def post(self,request):
        data = json.loads(request.body)
        product_id = data

        product = ProductModel.objects.get(PRODUCT_NO=product_id)

        dict_type_data = {"PRODUCT_NO": product.PRODUCT_NO, "PRODUCT_NAME": product.PRODUCT_NAME,
                          "PRODUCT_PRICE": product.PRODUCT_PRICE, "PRODUCT_QUANTITY": product.PRODUCT_QUANTITY
                          }
        json_data = json.dumps(dict_type_data)

        # json_data1 = serialize("json", [product],
        #                       fields=("PRODUCT_NO", "PRODUCT_NAME", "PRODUCT_PRICE", "PRODUCT_QUANTITY"))

        # json_data = json.dumps(json_data1)
        print(json_data)


        return HttpResponse(json_data,content_type="application/json")

@method_decorator(csrf_exempt,name="dispatch")
class Delete_product(View):
    def post(self,request):
        data = json.loads(request.body)
        product_id = data

        ProductModel.objects.get(PRODUCT_NO=product_id).delete()

        products_Data = ProductModel.objects.all()
        json_data = serialize("json", products_Data,
                              fields=("PRODUCT_NO", "PRODUCT_NAME", "PRODUCT_PRICE", "PRODUCT_QUANTITY"))

        print(json_data)

        return HttpResponse(json_data, content_type='application/json')

@method_decorator(csrf_exempt,name="dispatch")
class Update_product_data(View):
    def post(self, request):
        data = json.loads(request.body)
        product_no = data['product_no']
        product_name = data['product_name']
        price = data['price']
        quantity = data['quantity']

        product = ProductModel.objects.get(PRODUCT_NO=product_no)
        merchant_id = product.Merchant_Id_id

        ProductModel.objects.filter(PRODUCT_NO=product_no).update(PRODUCT_NO=product_no,PRODUCT_NAME=product_name,PRODUCT_PRICE=price,PRODUCT_QUANTITY=quantity,Merchant_Id=merchant_id)
        # return HttpResponse(json_data,content_type='application/json', status=200)

        products_Data = ProductModel.objects.all()
        json_data = serialize("json", products_Data,
                              fields=("PRODUCT_NO", "PRODUCT_NAME", "PRODUCT_PRICE", "PRODUCT_QUANTITY"))

        print(json_data)

        return HttpResponse(json_data, content_type='application/json')


def home_page(request):
    return render(request,"home_page.html")