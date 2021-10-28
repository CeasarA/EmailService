from django.urls import path
from .views import send_mail, send_sms



urlpatterns = [
    path('send/email/', send_mail),
    path('send/sms/', send_sms)
]
