from django.urls import path 
from .apiview import * 

app_name = 'qs_api'

urlpatterns = [
    path('question' , QuestionApiView.as_view() , name='question'),
    path('answer/<int:pk>' , AnswerQuestionView.as_view() , name='answer'),
    path('podcastqs/<int:pk>' , PodcastMainQs.as_view() , name='podcastqs'),
    path('user_coin' , CoinApiView.as_view() , name='user_coin'),
]