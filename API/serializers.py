from rest_framework import serializers
from . models import tweet

class tweetSerializer(Serializers.ModelSerializer):

    class Meta:
        model = tweet
        fields = '__all__'