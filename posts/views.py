from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from rest_framework import permissions, generics, status
from django.db.models import Count


class PostList(APIView):
    """
    List all posts
    No Create view (post method), as post creation handled by django signals
    """
    def get(self, request):
        posts = Post.objects.annotate(
            likes_count=Count('likes', distinct=True),
            comments_count=Count('comments', distinct=True)
        )
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PostSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(owner=request.user)  # Ensure Post model uses ForeignKey for this
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    "Retrieve, delete or update a post"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.annotate(
            likes_count=Count('likes', distinct=True),
            comments_count=Count('comments', distinct=True)
        )

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner != request.user and not request.user.is_superuser:
            return Response({'detail': 'Not allowed'}, status=status.HTTP_403_FORBIDDEN)
        return super().delete(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner != request.user and not request.user.is_superuser:
            return Response({'detail': 'Not allowed'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)
    
class ProfileMeView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.post