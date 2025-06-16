from rest_framework import generics
from .models import Challenge
from .serializers import ChallengeSerializer

class ChallengeListCreateView(generics.ListCreateAPIView):
    queryset = Challenge.objects.all().order_by('-start_date')
    serializer_class = ChallengeSerializer

class ChallengeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer