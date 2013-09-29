from django.http import HttpResponseRedirect
from django.conf.urls import patterns, include, url
from django.core.urlresolvers import resolve
from django.contrib import admin

class DummyUrlConf(object):
    pass

def redirect(request):
    #admin.site.urls
    if hasattr(request.user, 'medic') and request.user.medic:
        redirect = "patients/patient/"
        if 'patients' in request.path:
            redirect = "patient/"
        return HttpResponseRedirect(redirect)
    else:
        urlconf = DummyUrlConf()
        urlpatterns = patterns('',url(r'^admin/',
                    include(admin.site.urls)),
        )
        urlconf.urlpatterns = urlpatterns
        resolved = resolve(request.path, urlconf)
        return resolved[0](request)