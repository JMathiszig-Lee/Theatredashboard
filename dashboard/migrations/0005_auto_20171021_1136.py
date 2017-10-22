# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20171021_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oplist',
            name='Pat_ID',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='oplist',
            name='est_anaes_time',
            field=models.IntegerField(default=15),
        ),
        migrations.AlterField(
            model_name='oplist',
            name='est_surg_time',
            field=models.IntegerField(default=60),
        ),
        migrations.AlterField(
            model_name='oplist',
            name='op_ID',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='oplist',
            name='order',
            field=models.IntegerField(null=True),
        ),
    ]
