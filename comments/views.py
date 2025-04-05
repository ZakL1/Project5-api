from rest_framework import generics, permissions
from comments.models import Comment
from comments.serializers import CommentSerializer


class CommentList(generics.ListCreateAPIView):
    """
    Comment on a post, if user is logged in
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
