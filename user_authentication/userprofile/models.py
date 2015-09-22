from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
# Create your models here.
def get_upload_file_name(instance,filename):
        return 'uploaded_files/' + str(datetime.now())+'_' + filename
class UserProfile(models.Model):
    user=models.OneToOneField(User)
    avatar=models.FileField(upload_to=get_upload_file_name,null=True,blank=True)


    def save(self, *args, **kwargs):
            # delete old file when replacing by updating the file
            try:
                this = UserProfile.objects.get(id=self.id)
                if this.avatar != self.avatar:
                    this.avatar.delete(save=False)
            except: pass # when new photo then we do nothing, normal case
            super(UserProfile, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.user.username


@receiver(pre_delete, sender=UserProfile)
def article_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    if instance.avatar:
        instance.avatar.delete(False)

User.profile=property(lambda u: UserProfile.objects.get_or_create(user=u)[0])