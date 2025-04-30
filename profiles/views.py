from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework import generics, permissions, status


class ProfileList(APIView):
    """
    List all profiles
    No Create view (post method), as profile creation handled by django signals
    """
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True, context={'request': request})
        return Response(serializer.data)
    
class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    "Retrieve, delete or update profiles"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner != request.user:
            return Response({'detail': 'Not allowed'}, status=status.HTTP_403_FORBIDDEN)
        return super().delete(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner != request.user:
            return Response({'detail': 'Not allowed'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)
    
class ProfileMeView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile
    
    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx["request"] = self.request
        return ctx