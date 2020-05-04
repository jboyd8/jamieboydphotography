from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Contact(models.Model):
    contact_title = models.CharField(max_length=200)
    contact_body = models.TextField(blank=True)
    email = models.CharField(max_length=200)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    query_user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.contact_title
