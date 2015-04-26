from rest_framework import serializers

from recipemaster.recipes.models import Recipe, Tag


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        models = Tag
        fields = ('title', 'slug', 'color')


class RecipeSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        models = Recipe
        fields = ('title', 'url', 'tags')
