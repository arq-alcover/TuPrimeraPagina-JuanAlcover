from django.db import models
from django.contrib.auth.models import User
import os

def avatar_upload_path(instance, filename):
    return filename

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")  
    avatar = models.ImageField(upload_to=avatar_upload_path, blank=True, null=True)  
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    @property
    def avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        return "/static/images/default-avatar.png"  
