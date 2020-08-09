from votes.serializers import (
    VoteDetailSerializer, VoteListSerializer)
from rest_framework.permissions import (
    IsAuthenticated, IsAdminUser)
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from posts.models import Post
from users.models import User
from votes.models import Vote


class VoteView(generics.CreateAPIView):
    serializer_class = VoteDetailSerializer
    def post(self, request, pk):
        user = request.user.id
        if not Vote.objects.filter(user=user, post=pk).all():
            try:
                post = Post.objects.get(pk=pk)
                post.upvotes += 1
                post.save()
            except:
                return Response(data={"error": "post not found"},
                                status=status.HTTP_404_NOT_FOUND)
            user = User.objects.get(pk=user)
            Vote.objects.create(user=user, post=post)
            return Response(data={"response": "successfuly upvoted"},
                            status=status.HTTP_200_OK)
        return Response(data={"error": "user already upvoted post"},
                        status=status.HTTP_409_CONFLICT)
    permission_classes = (IsAuthenticated, )


class VoteListView(generics.ListAPIView):
    serializer_class = VoteListSerializer
    queryset = Vote.objects.all()
    permission_classes = (IsAdminUser, )
