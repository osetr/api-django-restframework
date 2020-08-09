from django.shortcuts import render
from rest_framework import generics
from posts.serializers import PostDetailSerializer, PostListSerializer
from posts.models import Post
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from posts.permissions import IsOwnerOrReadOnly


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostDetailSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    permission_classes = (IsAuthenticated,)


class PostListView(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()
    permissions = (IsAdminUser,)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
