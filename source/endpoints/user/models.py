from datetime import datetime

from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    language = models.CharField(max_length=30)
    media = models.TextField()
    last_seen = models.DateTimeField(default=datetime.now())


class RequestContact(models.Model):
    requester = models.OneToOneField(User, on_delete=models.CASCADE, related_name="requester")
    target = models.OneToOneField(User, on_delete=models.CASCADE, related_name="target")
    status = models.CharField(max_length=30, choices=(
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("declined", "Declined")
    ))
