from rest_framework import serializers
from qs_app.models import *

class QSSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainQuestion
        fields = ('__all__')

class QSAnswerSerializer(serializers.Serializer):
    user_correct_option_id = serializers.IntegerField()

class CoinSerializer(serializers.Serializer):
    time = serializers.IntegerField()
    