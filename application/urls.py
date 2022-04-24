from django.urls import path
from application import views

urlpatterns = [
    path('app/',views.hello_world),
]
