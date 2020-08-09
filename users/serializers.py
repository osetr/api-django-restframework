from rest_framework import serializers
from posts.models import Post
from users.models import User
from votes.models import Vote
from comments.models import Comment


class UserList(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = '__all__'
