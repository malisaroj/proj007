from rest_framework import serializers
from .models import User, Post, Comment

class UserSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta Class to map serializere's fields with the model fields."""
        model = User
        fields = ('id', 'username', 'user_email', 'gender', 'dob', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class PostSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta Class to map serializere's fields with the model fields."""
        model = Post
        fields = ('id', 'image', 'caption', 'user_id', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class CommentSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta Class to map serializere's fields with the model fields."""
        model = Comment
        fields = ('id', 'comment', 'user_id', 'post_id', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')