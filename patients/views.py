# -*- coding:utf-8 -*-
from django.http import HttpResponseRedirect
from django.conf.urls import patterns, include, url
from django.core.urlresolvers import resolve
from django.contrib import admin
from django.shortcuts import render

from patients.models import ChemotherapySchema
from patients.medical_calculations import (
    body_surface_area, corporal_mass_index, hematological_toxicity,
    non_hematological_toxicity, combined_toxicity
)


class DummyUrlConf(object):
    pass


def redirect(request):
    """
        If the user is a medic, redirect him to the index page.
    otherwise check the admin url pattern to check the view to redirect.
    """
    if hasattr(request.user, 'medic') and request.user.medic:
        redirect = "patients/index/"
        if 'patients' in request.path:
            redirect = "index/"
        return HttpResponseRedirect(redirect)
    else:
        urlconf = DummyUrlConf()
        urlpatterns = patterns('', url(r'^admin/',
                               include(admin.site.urls)),)
        urlconf.urlpatterns = urlpatterns
        resolved = resolve(request.path, urlconf)
        return resolved[0](request)


def medic_calculation(request):
    """
    Do the diferent calculations needed in a MedicalInterview.
    aivd, mna, mmt ,cmi
    """
    # variables used to get aivd
    can_use_phone = int(request.GET.get('can_use_phone'))
    can_walk = int(request.GET.get('can_walk'))
    can_shop = int(request.GET.get('can_shop'))
    can_cook = int(request.GET.get('can_cook'))
    can_do_home_work = int(request.GET.get('can_do_home_work'))
    can_do_manual_work = int(request.GET.get('can_do_manual_work'))
    can_self_sanitize = int(request.GET.get('can_self_sanitize'))
    can_take_medication = int(request.GET.get('can_take_medication'))
    can_manage_money = int(request.GET.get('can_manage_money'))

    aivd = (can_use_phone + can_walk + can_shop + can_cook + can_do_home_work +
            can_do_manual_work + can_self_sanitize + can_take_medication +
            can_manage_money)

    #varibales used to get mmt
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

    mmt = (orientation_date + orientation_place + record + atention_calculus +
           memory + lenguage_names + lenguage_repeat + lenguage_indicate +
           lenguage_obey + lenguage_draw + lenguage_write)

    #variables used to get mna
    stopped_eating = int(request.GET.get('stopped_eating'))
    lost_weight = int(request.GET.get('lost_weight'))
    movility = int(request.GET.get('movility'))
    had_stress = int(request.GET.get('had_stress'))
    neorologic_issues = int(request.GET.get('neorologic_issues'))

    mna = (stopped_eating + lost_weight + movility + had_stress +
           neorologic_issues)

    #other variables
    weight = float(request.GET.get('weight', 1))
    height = int(request.GET.get('size', 1))
    blood_presure = float(request.GET.get('diatolic_blood_pressure', 0))
    ldh = int(request.GET.get('ldh', 0))
    performanse_status = int(request.GET.get('performance_status', 0))
    scheme = int(request.GET.get("chemotherapy_scheme", None))

    cmi = corporal_mass_index(weight, height)
    bsa = body_surface_area(weight, height)

    if cmi < 19:
        ind_mna = 0
    elif cmi >= 19 and cmi < 21:
        ind_mna = 1
    elif cmi >= 21 and cmi < 23:
        ind_mna = 2
    else:
        ind_mna = 3

    mna += ind_mna

    #get chemotherapy risk from the model
    try:
        scheme = ChemotherapySchema.objects.get(pk=scheme)
        chemotherapy_risk = scheme.risk
    except:
        chemotherapy_risk = 0

    hematological_tox, hem_str = hematological_toxicity(blood_presure, ldh,
                                                        aivd,
                                                        chemotherapy_risk)

    non_hematological_tox, non_hem_str = non_hematological_toxicity(
        performanse_status, mmt, mna, chemotherapy_risk
    )

    comb_h_tox, comb_hem_str = combined_toxicity(non_hematological_tox,
                                                 hematological_tox,
                                                 chemotherapy_risk)

    return render(
        request, "patients/calculation.html",
        {'non_h_tox': non_hematological_tox,
         'h_toc': hematological_tox, 'sup_corp': bsa,
         'imc_d': cmi, 'aivd': aivd, 'mmt': mmt, 'mna': mna,
         'comb_h_tox': comb_h_tox, 'comb_hem_str': comb_hem_str,
         'non_hem_str': non_hem_str, 'hem_str': hem_str}
    )


def app_index(request):
    return render(request, "patients/app_index.html", {})
