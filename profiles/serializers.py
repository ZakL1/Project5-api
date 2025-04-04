from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()

    class Meta:
        model = Profile
        fields = [
            'id', 'is_owner', 'owner', 'created_at', 'updated_at', 'name',
            'content', 'image', 'posts_count', 
        ]

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner