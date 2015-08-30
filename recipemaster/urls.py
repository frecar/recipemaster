from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView


urlpatterns = patterns(
    '',
    url(r'^$', RedirectView.as_view(url=reverse_lazy('recipes:index'))),
    url(r'^recipes/', include('recipemaster.recipes.urls', namespace='recipes')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('recipemaster.api.urls')),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'},
        name='logout'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
)
