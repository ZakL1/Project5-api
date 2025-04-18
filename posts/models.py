from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

class Post(models.Model):
    """
    Post model, for created posts
    """
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
        return f'{self.id} {self.title}'

    def save(self, *args, **kwargs):
        # Call original save method to ensure we have an image file
        super().save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image)
            output = BytesIO()

            # Resize the image (change dimensions here)
            img = img.convert('RGB')  # In case image is RGBA or other mode
            img = img.resize((800, 600), Image.ANTIALIAS)

            # Save to BytesIO object
            img.save(output, format='JPEG', quality=85)
            output.seek(0)

            # Save resized image back to the image field
            self.image.save(self.image.name, ContentFile(output.read()), save=False)
            super().save(*args, **kwargs)  # Save again after resizing
            img.save(self.image.path, format='JPEG', quality=85)
