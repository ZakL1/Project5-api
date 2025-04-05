from django.urls import path
from likes import views
from .views import LikeList, LikeDetail

urlpatterns = [
    path('likes/', views.LikeList.as_view()),
    path('likes/<int:pk>/', LikeDetail.as_view(), name='like-detail'),
]