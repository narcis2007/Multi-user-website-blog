from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    title=models.CharField(max_length=256)
    content=models.TextField()
    email=models.EmailField()