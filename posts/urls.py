from django.urls import path
from posts import views
from .views import PostList, PostDetail

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
]