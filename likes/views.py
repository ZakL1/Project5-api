from rest_framework import generics, permissions
from likes.models import Like
from likes.serializers import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    """
    List likes or like a post if logged in
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LikeDetail(generics.RetrieveDestroyAPIView):
    "Retrieve or delete a like"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner != request.user:
            return Response({'detail': 'Not allowed'}, status=status.HTTP_403_FORBIDDEN)
        return super().delete(request, *args, **kwargs)