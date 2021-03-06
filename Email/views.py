from logging import error
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse

from .models import EmailModel, PhoneModel
from .serializers import EmailSerializer

from Config.email_main import prepare_email
from Config.sms_main import sending_sms

# Create your views here.
def send_mail(request, *args, **kwargs):
        if request.method == 'POST':
            try:
                email = request.POST['email']
                EmailModel.objects.create(
                    email=email,
                )
                print('email saved!')
                email_dict = {
                    'email': email,
                }
                prepare_email(email)
                print(email)
                return JsonResponse(data=email_dict, status=200, safe=False)
            except Exception as e:
                print("Error", e)
                return JsonResponse(data=e)
        
        elif request.method == 'GET':
            return render(request, "Email/send-email.html")

def send_sms(request,  *args, **kwargs):
    if request.method == 'POST':
        phone = request.POST['phone']
        clean_phone = '+233' + str(phone[1:])
        PhoneModel.objects.create(
            phone=clean_phone,
        )
        print('phone saved!', clean_phone)
        phone_dict = {
            'phone': clean_phone,
        }
        try:
            print('clean', clean_phone)
            sending_sms(clean_phone)
            return JsonResponse(data=phone_dict, status=200, safe=False)
        except Exception as e:
            print('Error', e)
            return JsonResponse(data=e, safe=False)
    elif request.method == 'GET':
        return render(request, "Email/send-sms.html")


def home(request):
    return render(request, "Email/home.html")
