from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone = models.CharField(max_length=13,null=False,blank=True)

    REQUIRED_FIELDS = ['email','phone']
    def __str__(self):
        return self.username