from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crashplusplus.views.home', name='home'),
    # url(r'^crashplusplus/', include('crashplusplus.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/patients/',include('patients.urls')),
    (r'^admin/$', 'patients.views.redirect'),
    (r'^admin/patients/$', 'patients.views.redirect'),
    url(r'^admin/', include(admin.site.urls)),

)
