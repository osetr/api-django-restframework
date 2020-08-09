from rest_framework import serializers
from posts.models import Post, User
from votes.models import Vote
from comments.models import Comment


class VoteListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Vote
            fields = '__all__'

class VoteDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Vote
        fields = '__all__'
