# models.py
from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    description = models.TextField()
    event_date = models.DateField()
    image = models.ImageField(upload_to='events/images/')  # Adjust the upload_to path as needed

    def __str__(self):
        return self.title
