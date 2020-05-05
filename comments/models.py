from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from blog.models import Blogs


class BlogComment(models.Model):
    """
    Creates a model for once instance of a blog comment.
    """
    comment_body = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    related_blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.comment_body
