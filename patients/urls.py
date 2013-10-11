from django.conf.urls.defaults import *

urlpatterns = patterns('patients.views',
    url(r'results/$', 'medic_calculation', name='results'),
    url(r'index/$', 'app_index', name='app_index'),
)