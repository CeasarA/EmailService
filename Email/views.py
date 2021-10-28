from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status

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


@api_view(['POST'])
def send_sms(request):
    if request.method == 'POST':
        phone = request.data['phone']
        clean_phone = '+233' + str(phone[1:])
        PhoneModel.objects.create(
            phone=clean_phone,
        )
        print('phone saved!', clean_phone)
    try:
        send_sms(clean_phone)
    except Exception as e:
        print('Error', e)

    return JsonResponse(data=request.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def home(request):
    return render("home friend!")