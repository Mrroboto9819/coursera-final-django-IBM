from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    username = models.CharField(unique=True, max_length=100, default="", blank=True, null=True)
    email = models.EmailField(
        max_length=500)
    
    name = models.CharField(max_length=100, default="", blank=True, null=True)
    lastname = models.CharField(max_length=100, default="", blank=True, null=True)

    # Add your custom fields here
    def __str__(self):
      return self.email