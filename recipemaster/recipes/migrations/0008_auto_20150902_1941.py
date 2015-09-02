# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_recipe_creation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='html_content',
            field=models.TextField(default=datetime.datetime(2015, 9, 2, 17, 41, 32, 387563, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='recipes', to='recipes.Tag'),
            preserve_default=True,
        ),
    ]
