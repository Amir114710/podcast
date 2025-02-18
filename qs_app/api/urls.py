from django.urls import path 
from .apiview import * 

app_name = 'qs_api'

urlpatterns = [
    path('question' , QuestionApiView.as_view() , name='question'),
    path('answer/<int:pk>' , AnswerQuestionView.as_view() , name='answer'),
    path('podcastqs/<int:pk>' , PodcastMainQs.as_view() , name='podcastqs'),
    path('user_coin' , CoinApiView.as_view() , name='user_coin'),
    path('hint/<int:pk>' , HintQuestionsView.as_view() , name='hint'),
    path('podcast_hints/<int:pk>' , QuestionHintList.as_view() , name='podcast_hints')
]