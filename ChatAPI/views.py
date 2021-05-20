from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse, response

from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import parser_classes
from ChatModel.talktobot import ChatBot
# from ChatAPI.serializers import PatternSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'ChatBot Response': '/chat/',
        'Custom Response': '/custom-response/tag/',
        'Get Tags': '/tags/',
    }
    return Response(api_urls)


@api_view(['POST'])
@parser_classes([JSONParser])
def Chat(request):
    serializer = "d"
    if serializer:
        response = ChatBot(request.data["pattern"])
    else:
        response = "ERROR"
    return Response(response)
