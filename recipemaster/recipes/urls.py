from django.conf.urls import patterns, url

from recipemaster.recipes import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^by-tag/(?P<tag_id>\d+)/$', views.tag_filter, name='tag_filter')
)
