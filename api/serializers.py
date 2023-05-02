from rest_framework import serializers

from account.models import User
from blog.models import Post
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username']
class PostSerializer(serializers.ModelSerializer):
    author=UserSerializer(read_only=True)
    class Meta:
        model=Post
        fields='__all__'