from django.urls import path
from .apiview import *

app_name = 'podcast_api'

urlpatterns = [
    #singer
    path('singer_list' , SingerListApiView.as_view() , name='singer_list'),
    path('singer_detail/<int:pk>' , SingerDetailApiView.as_view() , name='singer_detail'),
    path('singer/favorite/<int:pk>' , SingerFavoriteCreateView.as_view() , name='singer_favorite'),
    path('singer/favorite/list/<int:pk>' , SingerFavoriteListView.as_view() , name='singer_favorite_list'),
    path('TheBest_singer' , TheBestSingerListView.as_view() , name='TheBest_singer'),
    #music
    path('podcast_list' , PodcastListApiView.as_view() , name='podcast_list'),
    path('podcast_detail/<str:slug>' , PodcastDetailApiView.as_view() , name='podcast_detail'),
    path('category/list' , CategoryListView.as_view() , name='categories'),
    path('category/detail/<int:pk>' , CategoryDetailView.as_view() , name='category_detail'),
    path('podcast/favorite/<slug:slug>' , PodcastFavoriteCreateView.as_view() , name='podcast_favorite'),
    path('podcast/favorite/list/<slug:slug>' , PodcastFavoriteListView.as_view() , name='podcast_favorite_list'),
    path('podcast/favorite/user_list/<slug:slug>' , PodcastFavoriteUserListView.as_view() , name='podcast_favorite_user_list'),
    path('TheLastestMusic' , TheBestPodcastView.as_view() , name='the_best_podcast_view'),
    path('playlist/<int:pk>' , PlaylistDetailView.as_view() , name='playlist_detail'),
    path('playlist/' , PlaylistListApiView.as_view() , name='playlist_list'),
    path('podcast/save/<slug:slug>' , PodcastSaveCreateView.as_view() , name='podcast_save'),
    path('podcast/save/list/<slug:slug>' , PodcastSaveListView.as_view() , name='podcast_save_list'),
    path('podcast/save/user_list/<slug:slug>' , PodcastSaveUserListView.as_view() , name='podcast_save_user_list'),
]