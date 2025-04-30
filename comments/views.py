from rest_framework import generics, permissions
from comments.models import Comment
from comments.serializers import CommentSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from posts.models import Post


class CommentList(generics.ListCreateAPIView):
    """
    Comment on a post, if user is logged in
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.request.data.get('post')) 
        serializer.save(owner=self.request.user, post=post)

    def get_queryset(self):
        post_id = self.request.query_params.get('post')
        if post_id:
            return Comment.objects.filter(post_id=post_id)
        return Comment.objects.none()


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    "Retrieve or delete a comment"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner != request.user:
            return Response({'detail': 'Not allowed'}, status=status.HTTP_403_FORBIDDEN)
        return super().delete(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner != request.user and not request.user.is_superuser:
            return Response({'detail': 'Not allowed'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)
    
class ProfileMeView(generics.RetrieveAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.comment
