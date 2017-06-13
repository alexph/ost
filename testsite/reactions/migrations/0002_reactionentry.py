# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('episodes', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('reactions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReactionEntry',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('deleted', models.BooleanField(default=False)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('episode', models.ForeignKey(to='episodes.Episode', related_name='reactions')),
            ],
        ),
    ]
