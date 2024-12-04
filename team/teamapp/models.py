from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Member(AbstractUser):
    created = models.DateTimeField(auto_now_add=True)
    first = models.CharField(max_length=256)
    last = models.CharField(max_length=256)
    email = models.EmailField(max_length=256, unique=True)
    phone = models.CharField(max_length=256, unique=True)
    role = models.CharField(choices=[('Regular', "Can't delete members"), ('Admin', 'Can delete members')], default='Regular', max_length=100)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ['last']