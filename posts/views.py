from django.shortcuts import render
from rest_framework import generics
from posts.serializers import (
    PostDetailSerializer, PostListSerializer)
from comments.serializers import CommentDetailSerializer
from votes.serializers import VoteDetailSerializer, VoteListSerializer
from rest_framework import serializers
from posts.permissions import IsOwnerOrReadOnly
from posts.models import Post, User
from votes.models import Vote
from comments.models import Comment
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

class CommentDetailView(generics.CreateAPIView):
    def post(self, request, pk):
        content = request.data['content']
        user=User.objects.get(pk=request.user.id)
        post = Post.objects.get(pk=pk)
        Comment.objects.create(author=user, post=post, content=content)
        return Response(status=status.HTTP_201_CREATED)
    def get(self, request, pk):
        queryset = Comment.objects.all()
        return Response(CommentDetailSerializer(queryset, many=True).data, status=status.HTTP_201_CREATED)
    permission_classes = (IsAuthenticated, )

class CommentUpdateView(generics.CreateAPIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404
    def put(self, request, pk):
        obj = self.get_object(pk)
        obj.content = request.data['content']
        obj.save()
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_201_CREATED)
    permission_classes = (IsAuthenticated, )


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
