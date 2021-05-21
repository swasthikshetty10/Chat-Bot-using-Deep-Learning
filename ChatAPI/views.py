from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, response
from tensorflow.python.keras.optimizers import serialize
from .serializers import PatternSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ChatModel.talktobot import ChatBot
from .models import Pattern
# from ChatAPI.serializers import PatternSerializer


@api_view(['GET'])
def api_Overview(request):
    api_urls = {
        'ChatBot Response': '/chat/<str:pattern>',
        'Custom Response': '/custom-response/tag/',
    }
    return Response(api_urls)


@api_view(['GET'])
def Chat(request, pattern):
    response = ChatBot(pattern)
    return Response(response)


@api_view(['POST'])
def Chat_(request):
    """
    {
        "value" : "Your query"
    }
    """
    print(request.data)
    serializer = PatternSerializer(request.data)
    try:
        response = ChatBot(serializer.data["value"])
    except:
        response = {
            "error": "Data is in wrong formate use { 'value' : 'Your query' }",
            "response": None,
            "tag": None
        }
    return Response(response)

# @api_view(['GET'])
# def Tags(request, pattern):

#     return Response(response)
