from rest_framework import generics
from posts.serializers import (
    PostDetailSerializer, PostListSerializer)
from comments.serializers import CommentDetailSerializer
from votes.serializers import VoteDetailSerializer, VoteListSerializer
from posts.models import Post, User
from votes.models import Vote
from comments.models import Comment
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.response import Response

class CommentCreateView(generics.CreateAPIView):
    def post(self, request, pk):
        content = request.data['content']
        user=User.objects.get(pk=request.user.id)
        post = Post.objects.get(pk=pk)
        Comment.objects.create(author=user, post=post, content=content)
        return Response(status=status.HTTP_201_CREATED)
    permission_classes = (IsAuthenticated, )

class CommentGetView(generics.CreateAPIView):
    def get(self, request, pk):
        queryset = Comment.objects.get(pk=pk)
        return Response(CommentDetailSerializer(queryset).data, status=status.HTTP_201_CREATED)
    permission_classes = (IsAuthenticated, )

class CommentGetAllView(generics.CreateAPIView):
    def get(self, request):
        queryset = Comment.objects.all()
        return Response(CommentDetailSerializer(queryset, many=True).data, status=status.HTTP_201_CREATED)
    permission_classes = (IsAuthenticated, IsAdminUser)

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
    permission_classes = (IsAuthenticated, )

class CommentDeleteView(generics.CreateAPIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404
    def delete(self, request, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_201_CREATED)
    permission_classes = (IsAuthenticated, )
