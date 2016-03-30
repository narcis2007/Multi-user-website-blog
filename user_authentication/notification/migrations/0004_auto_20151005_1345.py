# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0003_auto_20151005_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='viewed',
            field=models.ManyToManyField(related_name='notification_viewed', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
