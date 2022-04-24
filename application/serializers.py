from rest_framework import serializers
from .models import Users,Books,Orders

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id','first_name','last_name','email']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['bookId','BookName','category']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['full_name','Book','orderId','IssueDate','returnDate']


