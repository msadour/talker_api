from datetime import datetime

from django.db import models

from source.endpoints.user.models import User


class Story(models.Model):

    message = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now())
    media = models.TextField()
