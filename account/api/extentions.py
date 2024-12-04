from django.core.mail import send_mail 
import random 
from account.models import User 
from config import settings
 
from django.core import mail 
connection = mail.get_connection() 
 
def send_otp_via_email(email): 
    subject = 'Your account verification email' 
    otp = random.randint(1000, 9999) 
    message = f'Your otp is {otp}' 
    email_from = settings.EMAIL_HOST 
    email_user = settings.EMAIL_HOST_USER 
    email_password = settings.EMAIL_HOST_PASSWORD 
    connection.open() 
    email_otp = mail.EmailMessage( 
        subject, 
        message, 
        email_user, 
        [email], 
        connection=connection, 
    ) 
    email_otp.send() 
    # send_mail(subject, message, email_user, email) 
    connection.close() 
    user_obj = User.objects.get(email=email) 
    user_obj.password = otp 
    print(otp)
    user_obj.save()