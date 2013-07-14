from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lending.views.home', name='home'),
    # url(r'^lending/', include('lending.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
