from django.conf.urls import include, url
from rest_framework import routers

from recipemaster.api.views import RecipeViewSet


router = routers.DefaultRouter()
router.register(r'recipes', RecipeViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
