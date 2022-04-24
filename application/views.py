from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

@api_view()
def hello_world(request):
    return Response({'msg':"hello world"},status=status.HTTP_200_OK)
