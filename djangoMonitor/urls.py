from django.conf.urls.defaults import patterns, include, url
from systemInfo import systemInfo
from resources import resources
from processes import processes
from fileSystems import fileSystems

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoMonitor.views.home', name='home'),
    # url(r'^djangoMonitor/', include('djangoMonitor.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', systemInfo),
    url(r'system/', systemInfo),
    url(r'processes/', processes),
    url(r'resources/', resources),
    url(r'filesystems/', fileSystems),
)
