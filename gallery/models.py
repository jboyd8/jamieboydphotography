from django.db import models
from datetime import datetime


class Gallery(models.Model):
    """Create the model for the gallery app"""

    image_title = models.CharField(max_length=200)
    image = models.URLField(default='https://image.flaticon.com/icons/svg/38/38645.svg')
    image_description = models.TextField(blank=True)
    is_published = models.BooleanField(default=False)
    date_added = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.image_title
