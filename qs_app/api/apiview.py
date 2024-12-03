from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from qs_app.models import *
from django.shortcuts import get_object_or_404 , render , redirect