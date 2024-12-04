from django.urls import path
from .apiview import *

app_name = 'api_account'

urlpatterns = [
    path('register' , RegisterApiView.as_view() , name='register'),
    path('login' , LogoinApiView.as_view() , name='login'),
    path('forget_password' , ForgetpasswordApiview.as_view() , name='forget_password'),
    path('profile' , UserProfileApiView.as_view() , name='profile'),
    path('online_user' , OnlineUserApiView.as_view() , name='online_user'),
]