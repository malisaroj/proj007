from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer, PostSerializer
from .models import User, Post
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

class UserView(generics.ListCreateAPIView):

    """This class defines the create behavior of our rest api."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new user."""
        serializer.save()


class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    if 'user' in cache:
        #get results from cache
        queryset = cache.get('user')

    else:
        queryset = User.objects.all()
        serializer_class = UserSerializer  
        # store data in cache
        cache.set('user', 'serializer_class', timeout=CACHE_TTL)


class PostView(generics.ListCreateAPIView):

    """This class defines the create behavior of our rest api."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new post."""
        serializer.save()


class PostDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer  