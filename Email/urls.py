from django.urls import path
from .views import send_mail, send_sms, home

app_name = "Email"

urlpatterns = [
    path('', home, name='home'),
    path('send/email/', send_mail, name='send-email'),
    path('send/sms/', send_sms, name="send-sms")
]
