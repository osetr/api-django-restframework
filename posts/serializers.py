from rest_framework import serializers
from posts.models import Post, User

class PostDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Post
        fields = '__all__'

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author']

class UserList(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = '__all__'
