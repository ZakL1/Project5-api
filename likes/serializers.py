from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Like model serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = Like
        fields = [
            'id', 'owner', 'created_at', 'post',    
        ]