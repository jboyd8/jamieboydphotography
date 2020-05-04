from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Contact(models.Model):
    """Create the contact model. create foreign key to the user table. This will allow us to see what user
    made an enquiry if they are logged in."""

    contact_title = models.CharField(max_length=200)
    contact_body = models.TextField(blank=True)
    email = models.CharField(max_length=200)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    query_user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.contact_title
