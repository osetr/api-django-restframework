from rest_framework import serializers
from posts.models import Post, User
from votes.models import Vote
from comments.models import Comment

class PostDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Post
        fields = '__all__'

class CommentDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Comment
        fields = '__all__'

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class UserList(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = '__all__'

class VoteListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Vote
            fields = '__all__'

class VoteDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Vote
        fields = '__all__'
