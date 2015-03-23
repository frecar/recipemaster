from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

urlpatterns = patterns(
    '',
    url(r'^$', RedirectView.as_view(url=reverse_lazy('recipes:index'))),

    url(r'^recipes/', include('recipemaster.recipes.urls', namespace='recipes')),
    url(r'^admin/', include(admin.site.urls)),
)
