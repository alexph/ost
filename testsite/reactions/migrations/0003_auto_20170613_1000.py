# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reactions', '0002_reactionentry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagereaction',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='imagereaction',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tweetreaction',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='tweetreaction',
            name='user',
        ),
        migrations.AddField(
            model_name='reactionentry',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 13, 10, 0, 40, 87564, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reactionentry',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
    ]
