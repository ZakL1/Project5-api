from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from rest_framework import permissions, generics


class PostList(APIView):
    """
    List all posts
    No Create view (post method), as post creation handled by django signals
    """
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response(serializer.data)
    
class PostDetail(generics.RetrieveDestroyAPIView):
    "Retrieve or delete a post"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner != request.user:
            return Response({'detail': 'Not allowed'}, status=status.HTTP_403_FORBIDDEN)
        return super().delete(request, *args, **kwargs)