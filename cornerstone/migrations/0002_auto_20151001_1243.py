# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cornerstone', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cornerstoneuserprofile',
            name='manager_id',
        ),
        migrations.AddField(
            model_name='cornerstoneuserprofile',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', blank=True, to='cornerstone.CornerstoneUserProfile', null=True),
        ),
        migrations.AlterField(
            model_name='cornerstoneuserprofile',
            name='guid',
            field=models.UUIDField(unique=True),
        ),
        migrations.AlterField(
            model_name='cornerstoneuserprofile',
            name='manager_guid',
            field=models.UUIDField(unique=True, null=True),
        ),
    ]
