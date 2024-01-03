# models.py
from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    description = models.TextField()
    event_date = models.DateField()
    image = models.ImageField(upload_to='events/images/') 

    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.description