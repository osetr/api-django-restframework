from rest_framework import serializers
from comments.models import Comment


class CommentDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Comment
        fields = '__all__'
