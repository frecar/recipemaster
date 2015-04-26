from rest_framework import routers

from recipemaster.api.views import RecipeViewSet


router = routers.DefaultRouter()
router.register(r'recipes', RecipeViewSet)

urlpatterns = router.urls
