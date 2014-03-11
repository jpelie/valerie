from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

from principal.views import qui, balde,valerie,pedro,Mhome

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'project.views.home', name='home'),
    #url(r'^$', 'home'),
    #url(r'^$',Mhome),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^qui/$',qui),
    #url(r'^contacts/$',balde),
    #url(r'^cours/$',pedro),
)
#urlpatterns += staticfiles_urlpatterns()
