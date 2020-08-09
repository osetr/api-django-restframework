from django.shortcuts import render
from rest_framework import generics
from posts.serializers import (
    PostDetailSerializer, PostListSerializer)
from users.serializers import UserList
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


class UserListView(generics.ListAPIView):
    serializer_class = UserList
    queryset = User.objects.all()
    permission_classes = (IsAdminUser, )
