from django.shortcuts import render
from rest_framework import generics
from posts.serializers import (
    PostDetailSerializer, PostListSerializer)
from comments.serializers import CommentDetailSerializer
from votes.serializers import VoteDetailSerializer, VoteListSerializer
from rest_framework import serializers
from posts.models import Post, User
from votes.models import Vote
from comments.models import Comment
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.response import Response


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
