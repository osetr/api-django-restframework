from rest_framework import serializers
from votes.models import Vote


class VoteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = "__all__"


class VoteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = "__all__"
