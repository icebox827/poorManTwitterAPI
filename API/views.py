from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.serializers import Serializer
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

    def post(self):
        pass
        # parser.add_argument("name")
        # parser.add_argument("content")
        # args = parser.parse_args
        # tweet_id = int(max(tweet.keys())) + 1
        # tweet_id = '%i' % tweet_id
        # tweet[tweet_id] = {
        #     "name": args["name"],
        #     "content": arg["content"]
        # }
        # return tweet[tweet_id], 201