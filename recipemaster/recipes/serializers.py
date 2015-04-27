from rest_framework import serializers

from recipemaster.recipes.models import Recipe, Tag


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('title', 'slug', 'color')


class RecipeSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ('title', 'url', 'tags')
