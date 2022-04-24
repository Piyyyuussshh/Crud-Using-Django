from collections import UserList
from django.urls import path
from .views import bookListCreate, bookRetrieveUpdateDelete, usersListCreate,userRetrieveUpdateDelete,ordersListCreate,orderRetrieveUpdateDelete
# from rest_framework.routers import DefaultRouter

# #created Router 
# router = DefaultRouter()

# #Register viewset with router


urlpatterns = [
    path('listCreate-users/',usersListCreate.as_view()),
    path('retrieveUpdateDelete-user/<int:pk>/',userRetrieveUpdateDelete.as_view()),
    path('listCreate-books/',bookListCreate.as_view()),
    path('retrieveUpdateDelete-book/<int:pk>/',bookRetrieveUpdateDelete.as_view()),
    path('listCreate-orders/',ordersListCreate.as_view()),
    path('retrieveUpdateDelete-order/<int:pk>/',orderRetrieveUpdateDelete.as_view()),
]
