from rest_framework import generics, permissions
from comments.models import Comment
from comments.serializers import CommentSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response


class CommentList(generics.ListCreateAPIView):
    """
    Comment on a post, if user is logged in
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveDestroyAPIView):
    "Retrieve or delete a comment"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner != request.user:
            return Response({'detail': 'Not allowed'}, status=status.HTTP_403_FORBIDDEN)
        return super().delete(request, *args, **kwargs)
