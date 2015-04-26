from rest_framework.viewsets import ViewSet

from recipemaster.api.permissions import ReadOnly
from recipemaster.recipes.models import Recipe
from recipemaster.recipes.serializers import RecipeSerializer


class RecipeViewSet(ViewSet):
    queryset = Recipe.objects.all()
    serializer = RecipeSerializer
    permission_classes = ReadOnly,
