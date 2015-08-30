# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorfield.fields


class Migration(migrations.Migration):
    dependencies = [
        ('recipes', '0003_auto_20150325_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='color',
            field=colorfield.fields.ColorField(max_length=10, default=''),
            preserve_default=False,
        ),
    ]
