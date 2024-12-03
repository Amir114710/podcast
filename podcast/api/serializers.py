from rest_framework import serializers
from podcast.models import *
#singer
class SingerFavoriteSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True , slug_field='email')
    singer = serializers.SlugRelatedField(read_only=True , slug_field='name')
    class Meta:
        model = SingerFavorite
        fields = ('__all__')

class SingerSerializer(serializers.ModelSerializer):
    playlist = serializers.SerializerMethodField()
    favorite = serializers.SerializerMethodField()
    podcast = serializers.SerializerMethodField()
    class Meta:
        model = Singer
        fields = ('__all__')
        read_only_fields = ('created','discrip')

    def get_playlist(self , obj):
        seri = PlaylistSerializer(instance=obj.playlists.all() , many=True)
        return seri.data

    def get_favorite(self , obj):
        seri = SingerFavoriteSerializer(instance=obj.singer_favorites.all() , many=True)
        return seri.data 
    
    def get_podcast(self , obj):
        podcast = obj.podcasts.all()
        seri = PodcastSerializer(instance=podcast , many=True)
        return seri.data

    
#music
class PodcastFavoriteSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True , slug_field='email')
    podcast = serializers.SlugRelatedField(read_only=True , slug_field='title')
    class Meta:
        model = PodcastFavorite
        fields = ('__all__')

class PodcastSaveSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True , slug_field='email')
    podcast = serializers.SlugRelatedField(read_only=True , slug_field='title')
    class Meta:
        model = PodcastSave
        fields = ('__all__')

class PodcastSerializer(serializers.ModelSerializer):
    singer = serializers.SlugRelatedField(read_only=True , slug_field='name')
    favorite = serializers.SerializerMethodField()
    save = serializers.SerializerMethodField()
    class Meta:
        model = Podcast
        fields = ('__all__')
        read_only_fields = ('created',)   

    def get_favorite(self , obj):
        seri = PodcastFavoriteSerializer(instance=obj.podcast_favorites.all() , many=True)
        return seri.data
    
    def get_save(self , obj):
        seri = PodcastSaveSerializer(instance=obj.podcast_saves.all() , many=True)
        return seri.data        

class CategorySerializer(serializers.ModelSerializer):
    podcast = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ('__all__')

    def get_podcast(self , obj):
        seri = PodcastSerializer(instance=obj.podcasts.all() , many=True)
        return seri.data
    
class PlaylistSerializer(serializers.ModelSerializer):
    singer = serializers.SlugRelatedField(read_only=True , slug_field='name')
    class Meta:
        model = PlayList
        fields = ('__all__')