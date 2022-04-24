import imp
from django.shortcuts import render
from .models import Users,Books,Orders
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework import status
from .serializers import UserSerializer,BookSerializer,OrderSerializer
from rest_framework.response import Response
from application import serializers
# Create your views here.

@api_view()
def hello_world(request):
    return Response({'msg':"hello world"},status=status.HTTP_200_OK)

#API FOR USERS MODEL

class usersListCreate(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    
class userRetrieveUpdateDelete(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

#API FOR BOOK MODEL

class bookListCreate(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

  
class bookRetrieveUpdateDelete(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)



# API FOR ORDER MODELS

class ordersListCreate(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class orderRetrieveUpdateDelete(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
