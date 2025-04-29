from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Like(models.Model):
    """
    Like model, for likes on a post
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        ordering = ['-created_at']
        unique_together = [['owner', 'post']]  # 1 like per user per post

    def __str__(self):
        return f'{self.owner} likes {self.post}'