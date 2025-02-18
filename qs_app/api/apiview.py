from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from qs_app.models import *
from django.shortcuts import get_object_or_404 , render , redirect
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
import random

class QuestionApiView(APIView):
    serializers_class = QSSerializer
    parser_classes = [MultiPartParser]
    def get(self , request):
        mainquestion = random.choice(MainQuestion.objects.all())
        seri = QSSerializer(mainquestion)
        return Response(seri.data , status=status.HTTP_200_OK)

class AnswerQuestionView(APIView):
    serializers_class = QSAnswerSerializer
    parser_classes = [MultiPartParser]
    def post(self , request , pk):
        data = request.data
        seria = QSAnswerSerializer(data=data)
        if seria.is_valid():
            main_question = get_object_or_404(MainQuestion , id=pk)
            user_correct_id = data['user_correct_option_id']
            user_correct_id_int = int(user_correct_id)
            if user_correct_id_int == main_question.correct_option.pk:
                main_question.correct_count = main_question.correct_count + 1
                main_question.save()
                return Response({'reponse':'correct'} , status=status.HTTP_200_OK)
            return Response({'reponse':'wrong'} , status=status.HTTP_400_BAD_REQUEST)   
        return Response(seria.errors , status=status.HTTP_400_BAD_REQUEST)
    
class CoinApiView(APIView):
    serializers_class = CoinSerializer
    parser_classes = [MultiPartParser]
    def get(self , request):
        user = request.user 
        data = request.GET
        time = data['time']
        time  = int(time)
        if time <= 5:
            user.coin += 20
            user.save()
        elif time >= 5:
            user.coin += 10
            user.save()
        else : 
            user.coin += 5
            user.save()
        return Response({'coin':user.coin} , status=status.HTTP_200_OK)
    
class PodcastMainQs(APIView):
    serializers_class = QSSerializer
    parser_classes = [MultiPartParser]
    def get(self , request , pk):
        podcast = get_object_or_404(Podcast , pk=pk)
        podcast_qs = MainQuestion.objects.filter(podcast=podcast)
        serializer = QSSerializer(podcast_qs , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)

class HintQuestionsView(APIView):
    serializers_class = HintSerializer
    parser_classes = [MultiPartParser]
    def get(self , request , pk):
        user = self.request.user
        hint = get_object_or_404(Hint , id=pk)
        user.coin -= hint.coin
        return Response({'coin':user.coin} , status=status.HTTP_200_OK)
    
class QuestionHintList(APIView):
    serializers_class = HintSerializer
    parser_classes = [MultiPartParser]
    def get(self , request , pk):
        podcast_hint = get_object_or_404(MainQuestion , id=pk)
        hints = podcast_hint.hints.all()
        seri = HintSerializer(hints , many=True)
        return Response(seri.data , status=status.HTTP_200_OK)