from django.shortcuts import render
from rest_framework import generics
from posts.serializers import PostDetailSerializer, PostListSerializer
from rest_framework import serializers
from .models import Post


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostDetailSerializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostListView(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
