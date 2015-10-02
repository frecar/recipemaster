# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('recipes', '0006_auto_20150327_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 28, 18, 40, 42, 337965, tzinfo=utc),
                                       auto_now_add=True),
            preserve_default=False,
        ),
    ]
