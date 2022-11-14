from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    student_id = models.CharField(max_length=10)
    profile_img = models.ImageField(null=True)
    content = models.TextField(null=True)