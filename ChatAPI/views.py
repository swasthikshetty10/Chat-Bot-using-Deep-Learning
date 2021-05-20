from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse, response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from ChatAPI.serializers import PatternSerializer

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'ChatBot Response' : '/chat/<srt:pattern>/',
        'Custom Response' : '/custom-response/tag/',
        'Get Tags' : '/tags/',
    }
    return Response(api_urls)