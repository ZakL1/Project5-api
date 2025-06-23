from rest_framework import generics, permissions
from likes.models import Like
from likes.serializers import LikeSerializer
from rest_framework import permissions, generics, status
from rest_framework.exceptions import PermissionDenied


class LikeList(generics.ListCreateAPIView):
    """
    List likes or like a post if logged in
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("You must be logged in to like a post.")
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveUpdateDestroyAPIView):
    "Retrieve or delete a like"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner != request.user:
            return Response({'detail': 'Not allowed'},
                            status=status.HTTP_403_FORBIDDEN)
        return super().delete(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner != request.user and not request.user.is_superuser:
            return Response({'detail': 'Not allowed'},
                            status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

   
class ProfileMeView(generics.RetrieveAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.like
