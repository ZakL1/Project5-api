from django.urls import path
from profiles import views
from .views import ProfileList, ProfileDetail, ProfileMeView

urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
    path('profiles/me/', ProfileMeView.as_view(), name='profile-me')
]