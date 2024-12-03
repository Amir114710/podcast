from django.db import models
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
import secrets

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, blank=True, null=True)
    username = models.CharField(max_length=350 , null=True)
    full_name = models.CharField(max_length=80 , null=True)
    phone_number = models.CharField(max_length=11)
    password_copy = models.TextField(null=True , blank=True)
    image = models.FileField(upload_to='user/image/' , null=True , blank=True , verbose_name='تصویر پروفایل')
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_online = models.BooleanField(default=False)
    subscription = models.BooleanField(default=False)
    otp = models.CharField(max_length=4, blank=True, null=True)
    # User Manager in ./managers.py
    objects = UserManager()
    date_added = models.DateField(auto_now_add=True , null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin
    
    class Meta:
        ordering = ('-date_added',)
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربرها'

class Advertising(models.Model):
    title = models.CharField(max_length=350 , null=True , blank=True , verbose_name='نام تبلیغات')
    image = models.FileField(upload_to='ad/image' , null=True , blank=True , verbose_name='تصویر تبلیغ')
    date_added = models.DateField(auto_now_add=True , null=True)

    class Meta:
        ordering = ('-date_added',)
        verbose_name = 'تبلیغ'
        verbose_name_plural = 'تبلیغات'

class PodcastRequest(models.Model):
    podcast_name = models.CharField(max_length=550 , null=True , verbose_name='نام پادکست')
    singer_name = models.CharField(max_length=550 , null=True , verbose_name='نام گوینده')
    date_added = models.DateField(auto_now_add=True , null=True)

    def __str__(self):
        return self.music_name
    
    class Meta:
        ordering = ('-date_added',)
        verbose_name = 'در خواست پادکست'
        verbose_name_plural = 'در خواست های پادکست'