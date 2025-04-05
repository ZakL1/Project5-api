from rest_framework import serializers
from .models import Post
from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    body = serializers.ReadOnlyField()

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'created_at',
            'body',             
        ]