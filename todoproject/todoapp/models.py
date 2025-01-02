from django.db import models

# Create your models here.
class ContactForm(models.Model):
    SERVICE_CHOICES = [
        ('data_explore', 'Data Exploration'),
        ('analytics_viz', 'Analytics and Visualization'),
        ('aiml_prediction', 'Prediction and Forecasting'),
        ('cad_modeling', 'CAD Modeling'),
        ('miscellaneous', 'Miscellaneous'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    service = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"

class Todo(models.Model):
    title = models.CharField(max_length=255)
    #description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
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