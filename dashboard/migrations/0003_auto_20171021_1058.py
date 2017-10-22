# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_checklist_oplist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='gone_collect',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='porter_sent',
            field=models.DateTimeField(null=True),
        ),
    ]
