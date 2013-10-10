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
        redirect = "patients/index/"
        if 'patients' in request.path:
            redirect = "index/"
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
    #aivd
    can_use_phone = int(request.GET.get('can_use_phone'))
    can_walk = int(request.GET.get('can_walk'))
    can_shop = int(request.GET.get('can_shop'))
    can_cook = int(request.GET.get('can_cook'))
    can_do_home_work = int(request.GET.get('can_do_home_work'))
    can_do_manual_work = int(request.GET.get('can_do_manual_work'))
    can_self_sanitize = int(request.GET.get('can_self_sanitize'))
    #taking_medication = int(request.GET.get('taking_medication'))
    can_take_medication = int(request.GET.get('can_take_medication'))
    can_manage_money = int(request.GET.get('can_manage_money'))


    aivd = can_use_phone + can_walk + can_shop + can_cook + can_do_home_work + \
        can_do_manual_work + can_self_sanitize + can_take_medication + can_manage_money

    #mmt
    orientation_date = int(request.GET.get('orientation_date'))
    orientation_place = int(request.GET.get('orientation_place'))
    record = int(request.GET.get('record'))
    atention_calculus = int(request.GET.get('atention_calculus'))
    memory = int(request.GET.get('memory'))
    lenguage_names = int(request.GET.get('lenguage_names'))
    lenguage_repeat = int(request.GET.get('lenguage_repeat'))
    lenguage_indicate = int(request.GET.get('lenguage_indicate'))
    lenguage_obey = int(request.GET.get('lenguage_obey'))
    lenguage_write = int(request.GET.get('lenguage_write'))
    lenguage_draw = int(request.GET.get('lenguage_draw'))


    mmt = orientation_date + orientation_place + record + atention_calculus + \
        memory + lenguage_names + lenguage_repeat + lenguage_indicate + \
        lenguage_obey + lenguage_draw + lenguage_write

    #mna
    stopped_eating = int(request.GET.get('stopped_eating'))
    lost_weight = int(request.GET.get('lost_weight'))
    movility = int(request.GET.get('movility'))
    had_stress = int(request.GET.get('had_stress'))
    neorologic_issues = int(request.GET.get('neorologic_issues'))

    mna = stopped_eating + lost_weight + movility + had_stress + neorologic_issues

    peso = float(request.GET.get('weight', 1))
    talla = int(request.GET.get('size', 1))
    tension_arterial = float(request.GET.get('diatolic_blood_pressure', 0))
    ldh = int(request.GET.get('ldh', 0))
    performanse_status = int(request.GET.get('performance_status', 0))
    scheme = int(request.GET.get("chemotherapy_scheme", None))

    indice_masa_corporal = round(peso/float(math.pow(talla/100.0,2)), 2)
    if indice_masa_corporal < 19:
        ind_mna = 0
    elif indice_masa_corporal >= 19 and indice_masa_corporal < 21:
        ind_mna = 1
    elif indice_masa_corporal >= 21 and indice_masa_corporal < 23:
        ind_mna = 2
    else:
        ind_mna = 3

    mna += ind_mna

    try:
        scheme = ChemotherapySchema.objects.get(pk=scheme)
        riesgo_por_quimio = scheme.risk
    except:
        riesgo_por_quimio = 0

    result = 0
    if tension_arterial > 72:
        result +=1
    if aivd < 26:
        result +=1
    if ldh > 459:
        result +=1
    comb_h_tox = result
    hematological_tox = result +  riesgo_por_quimio

    if hematological_tox in [0,1]:
        hem_str = "Riesgo bajo"
    elif hematological_tox in [2,3]:
        hem_str = "Riesgo intermedio bajo"
    elif hematological_tox in [4,5]:
        hem_str = "Riesgo intermedio alto"
    else:
        hem_str = "Alto Riesgo"


    result = 0
    if performanse_status in [1, 2]:
        result += 1
    elif performanse_status in [3, 4, 5]:
        result += 2
    if mmt < 30:
        result += 2
    if mna < 8:
        result += 2
    if peso <= 0:
        peso = 1
    if talla <= 0:
        talla = 1
    comb_h_tox += result + riesgo_por_quimio
    non_hematological_tox = result + riesgo_por_quimio

    if non_hematological_tox in [0,1,2]:
        non_hem_str = "Riesgo bajo"
    elif non_hematological_tox in [3,4]:
        non_hem_str = "Riesgo intermedio bajo"
    elif non_hematological_tox in [5,6]:
        non_hem_str = "Riesgo intermedio alto"
    else:
        non_hem_str = "Alto riesgo"

    if comb_h_tox in [0, 1, 2, 3]:
        comb_hem_str = "Riesgo bajo"
    elif comb_h_tox in [4,5,6]:
        comb_hem_str = "Riesgo intermedio bajo"
    elif comb_h_tox in [7,8,9]:
        comb_hem_str = "Riesgo intermedio alto"
    else:
        comb_hem_str = "Alto riesgo"

    #results
    superficie_corporal = round(math.sqrt((peso*talla)/3600.0), 2)
    indice_masa_corporal = round(peso/float(math.pow(talla/100.0,2)), 2)
    return render(request, "patients/calculation.html", {'non_h_tox': non_hematological_tox,
        'h_toc': hematological_tox, 'sup_corp': superficie_corporal,
        'imc_d': indice_masa_corporal, 'aivd': aivd, 'mmt': mmt, 'mna': mna,
        'comb_h_tox': comb_h_tox, 'comb_hem_str': comb_hem_str,
        'non_hem_str': non_hem_str, 'hem_str': hem_str})


def app_index(request):
    return render(request, "patients/app_index.html",{})

