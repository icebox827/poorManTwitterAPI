from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.serializers import Serializer
from rest_framework.parsers import JSONParser
from rest_framework import parsers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import tweet
from . serializers import tweetSerializer

# Create your views here.
class tweetList(APIView) :

    def get(self, request):
        tweet1 = tweet.objects.all()
        serializer=tweetSerializer(tweet1, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        parser_classes = (parsers.JSONParser)
        content = request.data["content"]
        name = request.data["name"]
        return Response()
        