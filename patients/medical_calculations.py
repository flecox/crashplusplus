# -*- coding:utf-8 -*-
import math


def body_surface_area(weight, height):
    return round(math.sqrt((weight*height)/3600.0), 2)


def corporal_mass_index(weight, height):
    if weight <= 0:
        weight = 1
    if height <= 0:
        height = 1
    return round(weight/float(math.pow(height/100.0, 2)), 2)


def hematological_toxicity(blood_presure, ldh, aivd, chemotherapy_risk):
    result = chemotherapy_risk
    if blood_presure > 72:
        result += 1
    if aivd < 26:
        result += 1
    if ldh > 459:
        result += 1

    if result in [0, 1]:
        hem_str = "Riesgo bajo"
    elif result in [2, 3]:
        hem_str = "Riesgo intermedio bajo"
    elif result in [4, 5]:
        hem_str = "Riesgo intermedio alto"
    else:
        hem_str = "Alto Riesgo"

    return (result, hem_str)


def non_hematological_toxicity(performanse_status, mmt, mna,
                               chemotherapy_risk):
    result = chemotherapy_risk
    if performanse_status in [1, 2]:
        result += 1
    elif performanse_status in [3, 4, 5]:
        result += 2
    if mmt < 30:
        result += 2
    if mna < 8:
        result += 2

    if result in [0, 1, 2]:
        non_hem_str = "Riesgo bajo"
    elif result in [3, 4]:
        non_hem_str = "Riesgo intermedio bajo"
    elif result in [5, 6]:
        non_hem_str = "Riesgo intermedio alto"
    else:
        non_hem_str = "Alto riesgo"

    return (result, non_hem_str)


def combined_toxicity(non_hematological_tox, hematological_tox,
                      chemotherapy_risk):
    result = non_hematological_tox + hematological_tox - chemotherapy_risk
    if result in [0, 1, 2, 3]:
        comb_hem_str = "Riesgo bajo"
    elif result in [4, 5, 6]:
        comb_hem_str = "Riesgo intermedio bajo"
    elif result in [7, 8, 9]:
        comb_hem_str = "Riesgo intermedio alto"
    else:
        comb_hem_str = "Alto riesgo"
    return(result, comb_hem_str)
