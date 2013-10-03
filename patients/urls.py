from django.conf.urls.defaults import *


urlpatterns = patterns('patients.views',
    url(r'^$', 'medic_calculation', name='results'),
)