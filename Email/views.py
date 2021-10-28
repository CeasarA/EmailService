from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse

from .models import EmailModel, PhoneModel
from .serializers import EmailSerializer

from Config.email_main import prepare_email
from Config.sms_main import send_sms

# Create your views here.
@api_view(['POST'])
def send_mail(request):
    if request.method == 'POST':
        email = request.data['email']
        EmailModel.objects.create(
            email=email,
            )
        print('email saved!')
    try:
        prepare_email(email)
    except Exception as e:
        print("Error", e)

    return JsonResponse(data=request.data, status=200)

# def send_sms(request, *args, **kwargs):
#     # return HttpResponse("Hello World")
#     if request.method == 'POST':
#         phone = request.POST['phone']
#         print(phone)
#         clean_phone = '+233' + str(phone[1:])
#         PhoneModel.objects.create(
#             phone=clean_phone,
#         )
#         print('phone saved!', clean_phone)
#     elif request.method == "GET":
#         return render(request, "Email/send-sms.html")

def send_sms(request,  *args, **kwargs):
    if request.method == 'POST':
        phone = request.POST['phone']
        clean_phone = '+233' + str(phone[1:])
        PhoneModel.objects.create(
            phone=clean_phone,
        )
        print('phone saved!', clean_phone)
        try:
            print(clean_phone)
            content = {
                "clean_phone" : clean_phone,
            }
            # send_sms(clean_phone)
            return HttpResponse(content)
        except Exception as e:
            print('Error', e)


    elif request.method == 'GET':
        return render(request, "Email/send-sms.html")


@api_view(['GET'])
def home(request):
    return render("home friend!")