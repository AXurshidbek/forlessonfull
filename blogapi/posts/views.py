from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework import permissions
from .permissions import *
from django.contrib.auth import get_user_model

class PostListAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer

class PostDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes =(IsAuthorOrReadOnly)
    # permission_classes = (IsAuthorOrReadOnly)
    queryset = Post.objects.all()
    serializer_class = PostsSerializer

class UserListAPIView(ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class PostModelaViewsSet(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly)
    queryset = Post.objects.all()
    serializer_class = PostsSerializer

class UserModelViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer