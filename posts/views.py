from django.shortcuts import render
from rest_framework import generics
from posts.serializers import PostDetailSerializer, PostListSerializer, UserList
from rest_framework import serializers
from posts.permissions import IsOwnerOrReadOnly
from posts.models import Post, User
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostDetailSerializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    permission_classes = (IsAuthenticated, )

class PostListView(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )

class UserListView(generics.ListAPIView):
    serializer_class = UserList
    queryset = User.objects.all()
    permission_classes = (IsAdminUser, )
