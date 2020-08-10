from rest_framework import generics
from comments.serializers import CommentDetailSerializer
from posts.models import Post
from users.models import User
from comments.models import Comment
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.response import Response


class CommentCreateView(generics.CreateAPIView):
    def post(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except:
            return Response(
                data={"error": "post not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        try:
            content = request.data["content"]
        except:
            return Response(
                data={"error": "'content' is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user = User.objects.get(pk=request.user.id)
        Comment.objects.create(author=user, post=post, content=content)
        return Response(
            data={"response": "successfully commented"},
            status=status.HTTP_201_CREATED
        )

    permission_classes = (IsAuthenticated,)


class CommentGetAllView(generics.CreateAPIView):
    def get(self, request):
        queryset = Comment.objects.all()
        return Response(
            CommentDetailSerializer(queryset, many=True).data,
            status=status.HTTP_201_CREATED,
        )

    permission_classes = (IsAdminUser,)


class CommentGetView(generics.CreateAPIView):
    def get(self, request, pk):
        try:
            queryset = Comment.objects.get(pk=pk)
        except:
            return Response(
                data={"error": "comment doesn't exist"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(
            CommentDetailSerializer(queryset).data,
            status=status.HTTP_201_CREATED
        )

    permission_classes = (IsAuthenticated,)


class CommentDeleteView(generics.CreateAPIView):
    def delete(self, request, pk):
        try:
            comment_obj = Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return Response(
                data={"error": "comment not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        if comment_obj.author.id == request.user.id:
            comment_obj.delete()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(
                data={"error": "you can't delete this comment"},
                status=status.HTTP_403_FORBIDDEN,
            )

    permission_classes = (IsAuthenticated,)


class CommentUpdateView(generics.CreateAPIView):
    def put(self, request, pk):
        try:
            comment_obj = Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return Response(
                data={"error": "comment not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        if comment_obj.author.id == request.user.id:
            try:
                comment_obj.content = request.data["content"]
            except:
                return Response(
                    data={"error": "'content' is required"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            comment_obj.save()
            return Response(
                data={"response": "successfully updated"},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                data={"error": "you can't update this comment"},
                status=status.HTTP_403_FORBIDDEN,
            )

    permission_classes = (IsAuthenticated,)
