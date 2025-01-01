from django.db import models
from martor.models import MartorField

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=255)
    #description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = MartorField() #models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Media(models.Model):
    title = models.CharField(max_length=200)  # Title of the media
    description = models.TextField(blank=True)  # Optional description
    image = models.URLField()  # URL of the media file in GCS
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return self.title