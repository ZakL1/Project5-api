from rest_framework import serializers
from .models import Challenge
from posts.models import Post
from posts.serializers import PostSerializer
from django.db.models import Count

class ChallengeSerializer(serializers.ModelSerializer):
    top_posts = serializers.SerializerMethodField()

    class Meta:
        model = Challenge
        fields = ['id', 'title', 'description', 'start_date', 'end_date', 'top_posts']

def get_top_posts(self, obj):
    top = Post.objects.filter(challenge=obj) \
        .annotate(likes_count=Count('likes', distinct=True)) \
        .order_by('-likes_count')[:3]
    return PostSerializer(top, many=True, context=self.context).data

