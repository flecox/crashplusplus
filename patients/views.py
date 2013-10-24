# -*- coding:utf-8 -*-
from django.http import HttpResponseRedirect
from django.conf.urls import patterns, include, url
from django.core.urlresolvers import resolve
from django.contrib import admin
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

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


@csrf_exempt
def medic_calculation(request):
    """
    Do the diferent calculations needed in a MedicalInterview.
    aivd, mna, mmt ,cmi
    """

    context = {}

    # variables used to get aivd
    can_use_phone = request.POST.get('can_use_phone', None)
    can_walk = request.POST.get('can_walk', None)
    can_shop = request.POST.get('can_shop', None)
    can_cook = request.POST.get('can_cook', None)
    can_do_home_work = request.POST.get('can_do_home_work', None)
    can_do_manual_work = request.POST.get('can_do_manual_work', None)
    can_self_sanitize = request.POST.get('can_self_sanitize', None)
    can_take_medication = request.POST.get('can_take_medication', None)
    can_manage_money = request.POST.get('can_manage_money', None)

    aivd_vars = (can_use_phone, can_walk,  can_shop,  can_cook,  can_do_home_work,
            can_do_manual_work,  can_self_sanitize,  can_take_medication,
            can_manage_money)

    can_aivd = True
    aivd = 0
    for var in aivd_vars:
        can_aivd = can_aivd and var is not None
        if can_aivd:
            aivd += int(var)

    context['aivd'] = aivd

    context['can_aivd'] = can_aivd

    #varibales used to get mmt
    orientation_date = request.POST.get('orientation_date', None)
    orientation_place = request.POST.get('orientation_place', None)
    record = request.POST.get('record', None)
    atention_calculus = request.POST.get('atention_calculus', None)
    memory = request.POST.get('memory', None)
    lenguage_names = request.POST.get('lenguage_names', None)
    lenguage_repeat = request.POST.get('lenguage_repeat', None)
    lenguage_indicate = request.POST.get('lenguage_indicate', None)
    lenguage_obey = request.POST.get('lenguage_obey', None)
    lenguage_write = request.POST.get('lenguage_write', None)
    lenguage_draw = request.POST.get('lenguage_draw', None)

    mmt_vars = (orientation_date, orientation_place, record,  atention_calculus,
           memory, lenguage_names, lenguage_repeat, lenguage_indicate,
           lenguage_obey, lenguage_draw, lenguage_write)

    can_mmt = True
    mmt = 0
    for var in mmt_vars:
        can_mmt = can_mmt and var is not None
        if can_mmt:
            mmt += int(var)
        context['mmt'] = mmt

    context['can_mmt'] = can_mmt

    #variables used to get mna
    stopped_eating = request.POST.get('stopped_eating', None)
    lost_weight = request.POST.get('lost_weight', None)
    movility = request.POST.get('movility', None)
    had_stress = request.POST.get('had_stress', None)
    neorologic_issues = request.POST.get('neorologic_issues', None)

    mna_vars = (stopped_eating, lost_weight, movility, had_stress,
           neorologic_issues)

    can_mna = True
    mna = 0
    for var in mna_vars:
        can_mna = can_mna and var is not None
        if can_mna:
            mna += float(var)

    #other variables
    weight = request.POST.get('weight', None)
    height = request.POST.get('size', None)
    blood_presure = request.POST.get('diatolic_blood_pressure', None)
    ldh = request.POST.get('ldh', None)
    performanse_status = request.POST.get('performance_status', None)
    scheme = request.POST.get("chemotherapy_scheme", None)

    can_weight = weight is not None and float(weight) > 0
    can_height = height is not None and float(height) > 0

    can_cmi = can_weight and can_height
    can_mna = can_mna and can_cmi
    if can_mna:
        cmi = corporal_mass_index(float(weight), int(height))

        if cmi < 19:
            ind_mna = 0
        elif cmi >= 19 and cmi < 21:
            ind_mna = 1
        elif cmi >= 21 and cmi < 23:
            ind_mna = 2
        else:
            ind_mna = 3

        mna += ind_mna
        context['mna'] = mna

    context['can_mna'] = can_mna

    #get chemotherapy risk from the model
    can_hem = True
    can_non_hem = True
    try:
        scheme = ChemotherapySchema.objects.get(pk=scheme)
        chemotherapy_risk = scheme.risk
    except:
        can_hem = False
        can_non_hem = False

    can_hem = can_hem and blood_presure is not None and ldh is not None and can_aivd

    if can_hem:
        hematological_tox, hem_str = hematological_toxicity(float(blood_presure), int(ldh),
                                                        int(aivd),
                                                        int(chemotherapy_risk))
        context['h_toc'] = hematological_tox
        context['hem_str'] = hem_str
    context['can_hem'] = can_hem

    can_non_hem = can_non_hem and performanse_status is not None and can_mmt and can_mna
    if can_non_hem:
        non_hematological_tox, non_hem_str = non_hematological_toxicity(
            int(performanse_status), int(mmt), int(mna), int(chemotherapy_risk)
        )
        context['non_h_toc'] = non_hematological_tox
        context['non_hem_str'] = non_hem_str
    context['can_non_hem'] = can_non_hem

    if can_non_hem and can_hem:
        comb_h_tox, comb_hem_str = combined_toxicity(non_hematological_tox,
                                                 hematological_tox,
                                                 chemotherapy_risk)
        context['comb_h_tox'] = comb_h_tox
        context['comb_hem_str'] = comb_hem_str
    return render(
        request, "patients/calculation.html",
        context
    )


def app_index(request):
    return render(request, "patients/app_index.html", {})
