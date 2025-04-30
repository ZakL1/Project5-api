from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from django.core.validators import MaxLengthValidator


class Comment(models.Model):
    """
    Comment model, for comments on a post
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(validators=[MaxLengthValidator(50)])

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner} {self.body}'