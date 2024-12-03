from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.parsers import MultiPartParser
from podcast.models import *
from .serializers import *
from rest_framework import filters
from account.api.serializers import UserSerializer

#singer

class SingerListApiView(APIView):
    serializers_class = SingerSerializer
    parser_classes = [MultiPartParser]
    def get(self , request):
        singers = Singer.objects.all()
        serializer = SingerSerializer(singers , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
class SingerDetailApiView(APIView):
    serializers_class = SingerSerializer
    parser_classes = [MultiPartParser]
    def get(self, request , pk):
        singer = get_object_or_404(Singer , id=pk)
        serializer = SingerSerializer(singer)
        return Response(serializer.data , status=status.HTTP_200_OK)

#podcast

class PodcastListApiView(APIView):
    serializers_class = PodcastSerializer
    parser_classes = [MultiPartParser]
    def get(self, request):
        podcasts = Podcast.objects.all()
        serializer = PodcastSerializer(podcasts , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
class PodcastDetailApiView(APIView):
    serializers_class = PodcastSerializer
    parser_classes = [MultiPartParser]
    def get(self , request , slug):
        podcast = get_object_or_404(Podcast , slug=slug)
        serializer = PodcastSerializer(podcast)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
#categories
class CategoryDetailView(APIView):
    serializer_class = PodcastSerializer
    parser_classes = [MultiPartParser]
    def get(self , request , pk):
        queryset = get_object_or_404(Category , id=pk).podcasts.all()
        serializer = PodcastSerializer(queryset , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
class CategoryListView(APIView):
    serializer_class = CategorySerializer
    parser_classes = [MultiPartParser]
    def get(self , request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)

#music save   
class PodcastSaveCreateView(APIView):
    serializer_class = PodcastSaveSerializer
    parser_classes = [MultiPartParser]
    def post(self , request , slug):
        save_model = get_object_or_404(Podcast , slug=slug)
        user = request.user
        if save_model.saves.filter(id=request.user.id).exists:
            save_model.saves.remove(request.user)
            saved = False
            save_model.save()
        save = PodcastSave.objects.create(user=user, podcast=save_model)
        save_model.saves.add(request.user)
        saved = True
        save_model.save()
        return JsonResponse({"save": saved})

class PodcastSaveListView(APIView):
    def get(self , request , slug):
        podcast = get_object_or_404(Podcast , slug=slug).podcast_saves.all()
        serializer = PodcastSaveSerializer(podcast , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)

class PodcastSaveUserListView(APIView):
    def get(self , request , slug):
        podcast_saves = get_object_or_404(Podcast , slug=slug).saves.all()
        seri = UserSerializer(podcast_saves , many=True)
        return Response(seri.data , status=status.HTTP_200_OK)
 
#music favorite   
class PodcastFavoriteCreateView(APIView):
    serializer_class = PodcastFavoriteSerializer
    parser_classes = [MultiPartParser]
    def post(self , request , slug):
        favorite_model = get_object_or_404(Podcast , slug=slug)
        user = request.user
        if favorite_model.likes.filter(id=request.user.id).exists:
            favorite_model.likes.remove(request.user)
            favorite_model.favorite_count -= 1
            liked = False
            favorite_model.save()
        favorite = PodcastFavorite.objects.create(user=user, podcast=favorite_model)
        favorite_model.likes.add(request.user)
        liked = True
        favorite_model.save()
        return JsonResponse({"liked": liked})

class PodcastFavoriteListView(APIView):
    def get(self , request , slug):
        podcast = get_object_or_404(Podcast , slug=slug).podcast_favorites.all()
        serializer = PodcastFavoriteSerializer(podcast , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
class PodcastFavoriteUserListView(APIView):
    def get(self , request , slug):
        podcast_favorite = get_object_or_404(Podcast , slug=slug).likes.all()
        seri = UserSerializer(podcast_favorite , many=True)
        return Response(seri.data , status=status.HTTP_200_OK)
    
class TheBestPodcastView(APIView):
    serializer_class = PodcastSerializer
    parser_classes = [MultiPartParser]
    def get(self , request):
        podcasts = Podcast.objects.all()
        for podcast in podcasts:
            if podcast.views >= 5:
                serializer = PodcastSerializer(podcasts , many=True)
                return Response(serializer.data , status=status.HTTP_200_OK)
            return HttpResponse('not found')

#singer favorite   
class SingerFavoriteCreateView(APIView):
    serializer_class = SingerFavoriteSerializer
    parser_classes = [MultiPartParser]
    def post(self , request , pk):
        singer = get_object_or_404(Singer , id=pk)
        user = request.user
        favorite = SingerFavorite.objects.create(user=user, singer=singer)
        singer.favorite_count += 1
        singer.likes.add(request.user)
        singer.save()
        serializer = PodcastFavoriteSerializer(favorite)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
class SingerFavoriteListView(APIView):
    serializer_class = SingerFavoriteSerializer
    parser_classes = [MultiPartParser]
    def get(self , request , pk):
        singer = get_object_or_404(Singer , id=pk).singer_favorites.all()
        serializer = SingerFavoriteSerializer(singer , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
class TheBestSingerListView(APIView):
    serializer_class = SingerSerializer
    parser_classes = [MultiPartParser]
    def get(self , request):
        singers = Singer.objects.all()
        for singer in singers:
            if singer.favorite_count > 5:
                serializer = SingerSerializer(singers , many=True)
                return Response(serializer.data , status=status.HTTP_200_OK)
            return HttpResponse('not found')
        
# playlist view
class PlaylistListApiView(APIView):
    serializers_class = PlaylistSerializer
    parser_classes = [MultiPartParser]
    def get(self , request):
        playlists = PlayList.objects.all()
        seri = PlaylistSerializer(playlists , many=True)
        return Response(seri.data , status=status.HTTP_200_OK)

class PlaylistDetailView(APIView):
    serializer_class = PlaylistSerializer
    parser_classes = [MultiPartParser]
    def get(self , request , pk):
        queryset = get_object_or_404(PlayList , id=pk)
        seri = PlaylistSerializer(queryset)
        return Response(seri.data , status=status.HTTP_200_OK)
    
# search view
class SearchApiListView(ListAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'english_title']    