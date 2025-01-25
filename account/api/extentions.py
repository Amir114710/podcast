from django.core.mail import send_mail 
import random 
from account.models import User 
from config import settings
 
from django.core import mail 
connection = mail.get_connection() 
 
# def send_otp_via_email(email): 
#     subject = 'Your account verification email' 
#     otp = random.randint(1000, 9999) 
#     message = f'Your otp is {otp}' 
#     email_from = settings.EMAIL_HOST 
#     email_user = settings.EMAIL_HOST_USER 
#     email_password = settings.EMAIL_HOST_PASSWORD 
#     connection.open() 
#     email_otp = mail.EmailMessage( 
#         subject, 
#         message, 
#         email_user, 
#         [email], 
#         connection=connection, 
#     ) 
#     email_otp.send() 
#     # send_mail(subject, message, email_user, email) 
#     connection.close() 
#     user_obj = User.objects.get(email=email) 
#     user_obj.password = otp 
#     print(otp)
#     user_obj.save()

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def send_otp_via_email(email):
    context = {}
    subject = 'New Password'
    message = random.randint(1000, 9999)
    if email:
        user = User.objects.get(email=email)
        user.password = message
        user.password_copy = message
        user.save()
        print(user.password_copy)
        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, [email])
            print('send')
            context['result'] = 'Email sent successfully'
        except Exception as e:
            print('error')
            context['result'] = f'Error sending email: {e}'
    else:
        context['result'] = 'All fields are required'