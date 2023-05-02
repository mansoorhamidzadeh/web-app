from django.shortcuts import render
from rest_framework.generics import *
from blog.models import Post
from .serializers import *


class PostApiView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



