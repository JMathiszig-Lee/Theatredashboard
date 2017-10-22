# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20171021_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklist',
            name='ready_code',
            field=models.IntegerField(default=0),
        ),
    ]
