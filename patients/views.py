# -*- coding:utf-8 -*-
from django.http import HttpResponseRedirect
from django.conf.urls import patterns, include, url
from django.core.urlresolvers import resolve
from django.contrib import admin
from django.shortcuts import render
import math

from patients.models import ChemotherapySchema

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

def medic_calculation(request):
    aivd = int(request.GET.get('aivd', 0))
    mmt = int(request.GET.get('mmt', 0))
    mna = int(request.GET.get('mna', 0))
    peso = float(request.GET.get('weight', 1))
    talla = int(request.GET.get('size', 1))
    tension_arterial = float(request.GET.get('diatolic_blood_pressure', 0))
    ldh = int(request.GET.get('ldh', 0))
    performanse_status = int(request.GET.get('performance_status', 0))
    scheme = int(request.GET.get("chemotherapy_scheme", None))

    try:
        scheme = ChemotherapySchema.objects.get(pk=scheme)
        riesgo_por_quimio = scheme.risk
    except:
        riesgo_por_quimio = 0
    #falta

    result = 0
    if tension_arterial > 72:
        result +=1
    if aivd < 26:
        result +=1
    if ldh > 459:
        result +=1

    hematological_tox = result +  riesgo_por_quimio

    result = 0
    if performanse_status in [1, 2]:
        result += 1
    elif performanse_status in [3, 4]:
        result += 2
    if mmt < 30:
        result += 2
    if mna < 8:
        result += 2

    non_hematological_tox = result + riesgo_por_quimio
    #results
    superficie_corporal = round(math.sqrt((peso*talla)/3600.0), 2)
    indice_masa_corporal = round(peso/float(math.pow(talla,2)), 2)
    return render(request, "patients/calculation.html", {'non_h_tox': non_hematological_tox,
        'h_toc': hematological_tox, 'sup_corp': superficie_corporal, 'imc_d': indice_masa_corporal})
