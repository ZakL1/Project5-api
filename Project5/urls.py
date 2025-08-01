"""
URL configuration for Project5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),  # Login, logout, etc.
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),  # Sign-up
    path('api/', include('profiles.urls')),  # profiles
    path('api/', include('posts.urls')),  # posts
    path('api/', include('likes.urls')),  # likes
    path('api/', include('comments.urls')),  # comments
    path('api/', include('challenges.urls')),  # challenges
]