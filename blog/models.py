from django.db import models

genres = [
    'Landscapes',
    'Portraits',
    'Cityscapes',
    'Technical',
    'General'
]


class Blogs(models.Model):
    """Create model for the blogs app"""

    blog_title = models.CharField(max_length=200)
    blog_body = models.TextField(blank=True)
    genre = models.CharField(choices=genres)
    date_added = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.blog_title
