from django.conf import settings 
from account.models import User 
from django.core import mail 
from random import randint
import ghasedakpack
import requests

sms = ghasedakpack.Ghasedak("f085742c7bafbef524c6885e74323428684b1543e72fe4a81681ae16af0f6183")
 
def send_otp_via_phone(phone_number): 
    subject = 'Your account verification phone' 
    random_code = randint(1000, 9999) 
    sms.verification({'receptor': phone_number , 'type': '1','template': 'musicapp','param1': random_code})
    user_obj = User.objects.get(phone_number=phone_number) 
    user_obj.otp = random_code 
    print(random_code)
    user_obj.save()