from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

# from django.http import JsonResponse
from portfolio.api import serializers
from portfolio.models import Question
from .serializers import votingSerializer



@api_view(['GET'])
def votingData(request):
    vote = Question.objects.all()
    backend = Question.objects.filter(answer='backend').count()
    frontend = Question.objects.filter(answer='frontend').count()
    fullstack = Question.objects.filter(answer='fullstack').count()
    # serializer = votingSerializer(vote, many=True)
    return Response({'backend':backend, 'frontend':frontend, 'fullstack':fullstack})