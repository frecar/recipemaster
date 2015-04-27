from rest_framework.viewsets import ModelViewSet

from recipemaster.api.permissions import ReadOnly
from recipemaster.recipes.models import Recipe
from recipemaster.recipes.serializers import RecipeSerializer


class RecipeViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = ReadOnly,
