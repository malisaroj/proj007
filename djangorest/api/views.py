from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer, PostSerializer
from .models import User, Post

class UserView(generics.ListCreateAPIView):

    """This class defines the create behavior of our rest api."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new user."""
        serializer.save()


class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = User.objects.all()
    serializer_class = UserSerializer  


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