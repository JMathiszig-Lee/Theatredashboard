# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20171021_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='oplist',
            name='Pat_ID',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='oplist',
            name='est_anaes_time',
            field=models.IntegerField(default=60, blank=True),
        ),
        migrations.AddField(
            model_name='oplist',
            name='est_surg_time',
            field=models.IntegerField(default=60, blank=True),
        ),
        migrations.AddField(
            model_name='oplist',
            name='op_ID',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='oplist',
            name='order',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
