from rest_framework import serializers
from account.models import User
from podcast.api.serializers import * 

class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    password_copy = serializers.CharField()
    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        User.objects.get_or_create(email=email , password=password)
        user = User.objects.get(email=email)
        return user
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(required=False)

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        User.objects.get_or_create(email=email , password=password)
        user = User.objects.get(email=email)
        return user
    
class UserSerializer(serializers.ModelSerializer):
    podcast_favorite = serializers.SerializerMethodField()
    podcast_save = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('__all__')

    def get_podcast_favorite(self , obj):
        podcast_favorite = obj.podcastlikes.all()
        seri = PodcastSerializer(podcast_favorite , many=True)
        return seri.data
    
    def get_podcast_save(self , obj):
        podcast_save = obj.podcastsaves.all()
        seri = PodcastSerializer(podcast_save , many=True)
        return seri.data