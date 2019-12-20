from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # pass
    username=models.CharField(max_length=30, unique=False)
    # add additional fields in here

    def __str__(self):
        return self.username