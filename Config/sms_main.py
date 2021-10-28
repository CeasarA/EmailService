from dotenv import load_dotenv
import os
import pprint
from twilio.rest import Client

load_dotenv()


TWILIO_ACCOUNT_SID= os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN=os.environ.get('TWILIO_AUTH_TOKEN')
SENDER_SMS=os.environ.get('SENDER_SMS')
RECIPIENT_SMS=os.environ.get('RECIPIENT_SMS')

# Authenticate SMS TOKEN
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

#  PREPARE THE MESSAGE 
content = 'This is a test trial SMS from your favorite Tech Company, Ceateck'


#  SEND AN SMS
def send_sms(phone):

    try:
        message = client.messages.create(to=phone, from_=SENDER_SMS, body=content)
        # # PARSE RESPONSE
        pp = pprint.PrettyPrinter(indent=4)

        print("----------------------")
        print("SMS")
        print("----------------------")
        print("RESPONSE: ", type(message))
        print("FROM:", message.from_)
        print("TO:", message.to)
        print("BODY:", message.body)
        print("PROPERTIES:")
        pp.pprint(dict(message._properties))
    except Exception as e:
        print("Error",e.body)
        return e

    return phone

# send_sms('+233246789484')
