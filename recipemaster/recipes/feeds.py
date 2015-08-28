# -*- coding: utf-8 -*-
from django.contrib.syndication.views import Feed

from .models import Recipe


class LatestRecipes(Feed):
    title = "Latest recipes"
    link = "/"

    def items(self):
        return Recipe.objects.all().order_by('-creation_date')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.render_text()

    def item_pubdate(self, item):
        return item.creation_date
