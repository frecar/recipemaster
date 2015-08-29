from django.conf.urls import patterns, url

from recipemaster.recipes.feeds import LatestRecipes

from recipemaster.recipes import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^by-tag/(?P<slug>[\w-]+)/$', views.tag_filter, name='tag_filter'),
    url(r'^feed/$', LatestRecipes()),
    url(r'^add/$', views.edit_recipe, name='add'),
    url(r'^(?P<recipe_id>\d+)/edit/$', views.edit_recipe, name='edit'),
    url(r'^(?P<recipe_id>\d+)/delete/$', views.delete_recipe, name='delete'),
    url(r'^collections/add/$', views.edit_collection, name='edit_collection'),
    url(
        r'^collections/(?P<collection_id>\d+)/edit/$',
        views.edit_collection,
        name='edit_collection'
    ),
    url(r'^collections/(?P<collection_id>\d+)/$', views.view_collection, name='view_collection'),
    url(r'^collections/(?P<collection_id>\d+)/remove/(?P<recipe_id>\d+)/$',
        views.remove_recipe_from_collection,
        name='remove_recipe_from_collection'
    ),
)
