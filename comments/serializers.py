from rest_framework import serializers
from comments.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    post = serializers.ReadOnlyField() 

    class Meta:
        model = Comment
        fields = ['id', 'owner', 'created_at', 'body', 'post']

    def validate_body(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Comment cannot be empty.")
        if len(value) > 100:
            raise serializers.ValidationError("Comment must be less than 100 characters long.")
        return value

