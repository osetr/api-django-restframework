from django.shortcuts import render
from rest_framework import generics
from posts.serializers import PostDetailSerializer, PostListSerializer, UserList, VoteDetailSerializer, VoteListSerializer
from rest_framework import serializers
from posts.permissions import IsOwnerOrReadOnly
from posts.models import Post, User, Vote
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.response import Response

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

class VoteView(generics.CreateAPIView):
    serializer_class = VoteDetailSerializer
    def post(self, request, user__id):
        user=request.user.id
        if not Vote.objects.filter(user=user, post=user__id).all():
            post = Post.objects.get(id=user__id)
            post.upvotes += 1
            post.save()
            user = User.objects.get(pk=user)
            post = Post.objects.get(pk=user__id)
            Vote.objects.create(user=user, post=post)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    permission_classes = (IsAuthenticated, )


class VoteListView(generics.ListAPIView):
    serializer_class = VoteListSerializer
    queryset = Vote.objects.all()
