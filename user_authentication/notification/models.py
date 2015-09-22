from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import messages
# Create your models here.

class Notification(models.Model):
    title=models.CharField(max_length=256)
    content=models.TextField()
    user=models.ForeignKey(User)
    viewed=models.BooleanField(default=False)

@receiver(post_save,sender=User)
def create_welcome_notification(sender,**kwargs):
    if kwargs.get('created',False):
        Notification.objects.create(user=kwargs['instance'],
                                    title='Welcome to our site',
                                    content='Thanks for signing up!'
                                    )

