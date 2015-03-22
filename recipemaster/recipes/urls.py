from django.conf.urls import patterns, url

from recipemaster.recipes import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<recipe_id>\d+)/$', views.recipe_detail, name='recipe_details'),
)
