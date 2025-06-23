from datetime import date
from rest_framework import generics
from .models import Challenge
from .serializers import ChallengeSerializer


class ChallengeListCreateView(generics.ListCreateAPIView):
    serializer_class = ChallengeSerializer

    def get_queryset(self):
        status = self.request.query_params.get("status")
        today = date.today()

        if status == "ongoing":
            return Challenge.objects.filter(
                start_date__lte=today,
                end_date__gte=today
            ).order_by("-start_date")
   
        elif status == "past":
            return Challenge.objects.filter(
                end_date__lt=today
            ).order_by("-start_date")
        else:
            return Challenge.objects.all().order_by("-start_date")


class ChallengeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
