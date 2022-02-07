from datetime import datetime

from django.db import models

from source.endpoints.user.models import User


class Chat(models.Model):
    participants = models.ManyToManyField(User)
    name = models.CharField(max_length=255)


class Message(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE, related_name="message_author")
    content = models.TextField()
    date = models.DateTimeField(default=datetime.now())
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="message_chat")
    status = models.CharField(max_length=255, choices=(
        ("sent", "Sent"),
        ("read", "Read")
    ))
