from django.urls import path
from comments import views
from .views import CommentList, CommentDetail

urlpatterns = [
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
]
