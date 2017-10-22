# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20171021_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='gone_collect',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='porter_sent',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
