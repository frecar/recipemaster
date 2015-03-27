# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
from recipemaster.recipes.models import Tag


def save_all_tags():
    """
    Save all tags to create slugs with autoslugfield
    """
    for tag in Tag.objects.all():
        tag.save()


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_tag_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False),
            preserve_default=True,
        ),
        migrations.RunPython(save_all_tags),
    ]
