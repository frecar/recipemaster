# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations, models


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
