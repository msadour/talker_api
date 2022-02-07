from django.db import models

from source.endpoints.user.models import User


class Settings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_settings")
    last_seen = models.CharField(max_length=255, choices=(
        ("everyone", "Everyone"),
        ("my_contact", "My contacts"),
        ("no_body", "Nobody")
    ))
    profile_photo = models.CharField(max_length=255, choices=(
        ("everyone", "Everyone"),
        ("my_contact", "My contacts"),
        ("no_body", "Nobody")
    ))
    status_viewers = models.ManyToManyField(User)

    enable_notification_for_message = models.BooleanField(default=True)

    theme_chat = models.CharField(max_length=255, choices=(
        ("light", "Light"),
        ("dark", "Dark"),
    ))
    theme_wallpaper = models.CharField(max_length=255, choices=(
        ("light", "Light"),
        ("dark", "Dark"),
    ))
