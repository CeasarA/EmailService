import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from celery import shared_task

load_dotenv()


SENDGRIP_API_KEY = os.environ.get('SENDGRIP_API_KEY')
MY_ADDRESS = os.environ.get('MY_ADDRESS')

# Authenticate SendAPI
client = SendGridAPIClient(SENDGRIP_API_KEY)

# Read email template
with open('./Config/email.html') as email_template:
    document = email_template.read()

# Prepare an Email
@shared_task
def prepare_email(email):
    subject = "Email Service Example"
    # content = "Hello Buddy,\n This is test trial of the email service. I hope you do not mind!"
    doc = document
    message = Mail(from_email=MY_ADDRESS, to_emails=email, subject=subject, html_content=doc)

    # ISSUE REQUEST 
    try:
        response = client.send(message)
        print(response.status_code)
        print(response.headers)
        print(response.body)
    except Exception as e:
        print("Error", e)
        print("Error Body", e.body)
        return e

    return message

