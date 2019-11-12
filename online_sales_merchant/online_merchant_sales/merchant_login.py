
import requests
import json

from django.http import request
from django.shortcuts import render



def merchant_login_verification(json_Data):

    res = requests.post("http://127.0.0.1:3000/login_merchant/",json_Data)


    # print(type(res))
    code = res.status_code

    # if res.status_code == 200:
    #     return render(request,"merchant_home.html")
    # else:
    #     return render(request,"home.html",{"message":"You Entered Wrong Details"})

    return res

