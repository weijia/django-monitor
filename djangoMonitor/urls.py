import settings
from django.conf.urls.defaults import patterns, include, url
from djangoMonitor.systemInfo.views import system
from djangoMonitor.resources.views import resources
from djangoMonitor.processes.views import processes
from djangoMonitor.fileSystems.views import fileSystems
import os

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
    url(r'^$', system),
    url(r'system/', system),
    url(r'processes/', processes),
    url(r'resources/', resources),
    url(r'filesystems/', fileSystems),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.FILE_UPLOAD_TEMP_DIR}),
)
