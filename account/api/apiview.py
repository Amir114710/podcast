from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from account.api.extentions import send_otp_via_email
from .serializers import *
from account.models import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.parsers import MultiPartParser
from .phone import send_otp_via_phone

# class RegisterApiView(APIView):
#     serializer_class = RegisterSerializer
#     parser_classes = [MultiPartParser]
#     def post(self, request):
#         data = request.data
#         serializer = RegisterSerializer(data=data)
#         if serializer.is_valid():
#             phone_number = data['phone_number']
#             username = data['username']
#             full_name = data['full_name']
#             User.objects.get_or_create(phone_number=phone_number , username=username , full_name=full_name)
#             user = User.objects.get(phone_number=phone_number)
#             Token.objects.get_or_create(user=user)
#             user.save()
#             send_otp_via_phone(phone_number=phone_number)
#             serializer.save()
#             return Response({'response': 'Added'}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LogoinApiView(APIView):
#     serializer_class = LoginSerializer
#     parser_classes = [MultiPartParser]
#     def post(self , request):
#         data = request.data
#         serializer = LoginSerializer(data=data)
#         if serializer.is_valid():
#             phone_number = serializer.data['phone_number']
#             user = User.objects.get(phone_number=phone_number)
#             if user is not None:
#                 if user.otp == serializer.data['otp']:
#                     user.otp = None
#                     user.is_active = True
#                     user.save()
#                     return Response(data={
#                         'Token': str(Token.objects.get(user=user)),
#                     })
                
#                 return Response(data={
#                     'otp_error': 'otp is wrong'
#                 }, status=status.HTTP_400_BAD_REQUEST)
#         return Response(serializer.errors , status=status.HTTP_200_OK)

class RegisterApiView(APIView):
    serializer_class = RegisterSerializer
    parser_classes = [MultiPartParser]
    def post(self , request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            email = data['email']
            password = data['password']
            password_copy = data['password_copy']
            if password_copy != password:
                return Response({'error':'passwords are not sames'} , status=status.HTTP_400_BAD_REQUEST)
            User.objects.get_or_create(email=email , password=password)
            user = User.objects.get(email=email)
            Token.objects.get_or_create(user=user)
            user.save()
            serializer.save()
            return Response({'response': 'Added' , 'token':str(Token.objects.get(user=user))}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoinApiView(APIView):
    serializer_class = LoginSerializer
    parser_classes = [MultiPartParser]
    def post(self , request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            email = serializer.data['email']
            password = serializer.data['password']
            user = User.objects.get(email=email)
            if user is not None:
                if user.password == serializer.data['password']:
                    user.is_active = True
                    user.save()
                    return Response(data={
                        'Token': str(Token.objects.get(user=user)),
                    })
                
                return Response(data={
                    'password_error': 'password is wrong'
                }, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors , status=status.HTTP_200_OK)
    
class ForgetpasswordApiview(APIView):
    serializers_class = ForgetPasswordSerializer
    parser_classes = [MultiPartParser]
    def post(self , request):
        data = request.data
        seri = ForgetPasswordSerializer(data=data)
        if seri.is_valid():
            email = seri.data['email']
            user = User.objects.get(email=email)
            send_otp_via_email(email)
            return Response({'data':user.password} , status=status.HTTP_200_OK)
        return Response(seri.errors , status=status.HTTP_200_OK)

class UserProfileApiView(APIView):
    serializers_name = UserSerializer
    parser_classes = [MultiPartParser]
    def get(self,request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
class OnlineUserApiView(APIView):
    serializers_class = UserSerializer
    parser_classes = [MultiPartParser]
    def get(self , request):
        online_user = User.objects.filter(is_online=True)
        seri = UserSerializer(online_user , many=True)
        return Response(seri.data , status=status.HTTP_200_OK)
