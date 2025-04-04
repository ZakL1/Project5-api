from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Post(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default2_lufpnp'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_post(sender, instance, created, **kwargs):
    if created:
        Post.objects.create(owner=instance)


post_save.connect(create_post, sender=User)