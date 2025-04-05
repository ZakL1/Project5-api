from django.urls import path
from profiles import views
from .views import ProfileList, ProfileDetail

urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
]