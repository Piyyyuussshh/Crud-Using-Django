from django.shortcuts import render
from rest_framework.filters import SearchFilter,OrderingFilter
from .models import Users,Books,Orders
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework import status
from .serializers import UserSerializer,BookSerializer,OrderSerializer
from rest_framework.response import Response
# Create your views here.

@api_view()
def hello_world(request):
    return Response({'msg':"hello world"},status=status.HTTP_200_OK)

#API FOR USERS MODEL
class usersListCreate(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ['first_name',]
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
    
    #Filter based on Books by matching name
    # filter_backends = [SearchFilter]
    # search_fields = ['^BookName']
    
    #List of all books grouped by category
    #Sort Orders by Order Date
    filter_backends = [OrderingFilter]
    ordering_fields = ['category',]
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def book_sort(request):
        return render(request,'application/index.html',{'queryset':queryset})

  
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
    ##Sorting the data by order_date
    serializer_class = OrderSerializer
    #Sort Orders by Order Date
    filter_backends = [OrderingFilter]
    ordering_fields = ['IssueDate',]
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