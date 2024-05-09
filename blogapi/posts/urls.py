from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *

urlpatterns=[
    path('users/', UserListAPIView.as_view()),
    path('users/<int:pk>', UserDetail.as_view()),
    path("<int:pk>", PostDetail.as_view()),
    path("", PostListAPIView.as_view()),

]