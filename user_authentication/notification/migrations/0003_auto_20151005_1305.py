# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notification', '0002_auto_20151005_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='user',
            field=models.ManyToManyField(related_name='notification_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='notification',
            name='viewed',
        ),
        migrations.AddField(
            model_name='notification',
            name='viewed',
            field=models.ManyToManyField(related_name='notification_viewed', to=settings.AUTH_USER_MODEL),
        ),
    ]
