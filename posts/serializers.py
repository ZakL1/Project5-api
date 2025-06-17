from rest_framework import serializers
from .models import Post
from likes.models import Like
from challenges.models import Challenge


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ImageField(source='owner.profile.image', read_only=True)
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    challenge = serializers.PrimaryKeyRelatedField(queryset=Challenge.objects.all(),
                                                    allow_null=True, required=False)

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'like_id',
            'likes_count', 'comments_count'
        ]

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None
