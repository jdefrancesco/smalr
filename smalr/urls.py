from django.conf.urls import patterns, include, url
from smalr.views import *


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'smalr.views.home', name='home'),
    # url(r'^smalr/', include('smalr.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^shorts/', include('shorts.urls')),
    url(r'^shorten/$', shorten),
    url(r'^(?P<key>\w+)$', redirect),
    url(r'', index),
)
