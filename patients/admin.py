# -*- coding:utf-8 -*-
from django.forms import ModelForm
from django.contrib import admin
from django import forms
from patients.models import Patient, MedicalInterview, Medic


class MedicAdmin(admin.ModelAdmin):
    pass

admin.site.register(Medic, MedicAdmin)


class MedicalInterviewAdminForm(ModelForm):
    """Additional display Fields for Profile"""
    body_surface_area = forms.FloatField(label="Superficie de área corporal", required=False)
    corporal_mass_index = forms.FloatField(label='Indice de masa corporal', required=False)

    class Meta:
        model = MedicalInterview

class MedicalInterviewAdmin(admin.StackedInline):
    model = MedicalInterview
    form = MedicalInterviewAdminForm
    extra = 0
    fieldsets = (
        (None, {
            'fields': ('date', ),
        }),
        (None, {'fields': (
            ('cie_10', 'stage', 'stage_observations', 'bone_compromised',),
            'prior_chemotherapies',
            ('number_comorbidity_categories', 'usual_medication'),
            ('cirs_g_index', 'cirs_g_severity_3'),
            'current_treatment_type',)}),
        (None, {'fields': (
            'performance_status',
            'falls')
        }),
        ("Escala de Actividades Instrumentales de la Vida Diaria", {'fields': (
            'can_use_phone', 'can_walk', 'can_shop', 'can_cook',
            'can_do_home_work', 'can_do_manual_work', 'can_self_sanitize',
            'taking_medication', 'can_take_medication', 'can_manage_money'),
            'classes': ('collapse',)
        }),
        ("Mini Mental State Examination", {"fields": (
            'orientation_date',
            'orientation_place', 'record', 'atention_calculus', 'memory',
            'lenguage_names', 'lenguage_repeat', 'lenguage_indicate',
            'lenguage_obey', 'lenguage_write', 'lenguage_draw'
        ),
            'classes': ('collapse',)
        }),
        (None, {'fields': (
            ('weight', 'size', 'body_surface_area', 'corporal_mass_index'),
            ('sistolic_blood_pressure', 'diatolic_blood_pressure'),
            'ldh')
        }),
        ("Mini Nutritional Assessment (MNA)", {"fields": (
            'stopped_eating', 'lost_weight', 'movility', 'had_stress',
            'neorologic_issues'
            ),
            'classes': ('collapse',)
        }),
        (None, {'fields': (
            'chemotherapy_scheme', 'dose_adjustment', 'discontinuation',
            'observations'),
        }),
    )


class PatientAdmin(admin.ModelAdmin):
    """
    Configuration for the Patient moel in the django admin.
    """
    name = "Paciente"
    list_display_links = ('name', 'last_name')
    list_display = ('name', 'last_name', 'clinical_history', 'dni')

    class Media:
        js = (
            "/static/patients/js/jquery.easyModal.js",
            "/static/patients/js/results.js"
        )

    inlines = [
        MedicalInterviewAdmin,
    ]

    fieldsets = (
        (None, {
            'fields': (
                ('clinical_history', 'dni'), ('name', 'last_name'),
                'born_date', 'genre', 'phone', 'study_level',
                'social_support'
                ),
        }),
    )

    search_fields = ['name', 'last_name', 'dni', 'clinical_history']

    def get_readonly_fields(self, request, obj=None):
        """
            If there's no edit in the url, we'll show the patient as readonly.
        """
        if 'edit' not in request.GET:
            return ('name', 'last_name', 'born_date', 'genre', 'dni',
                    'clinical_history', 'phone', 'study_level',
                    'social_support')
        else:
            return self.readonly_fields

    def change_view(self, request, object_id, form_url='', extra_context=None):
        """
            if we're seeing a patient (not editing or adding), we want to only
        show save button, to save the inline medical interviews.
        """
        extra_context = extra_context or {}
        if not request.GET.get('edit', False):
            extra_context['add'] = False
            extra_context['show_save'] = True
            extra_context['show_save_continue'] = False
            extra_context['show_save_continue'] = False
            extra_context['show_save_add'] = False
        return super(PatientAdmin, self).change_view(
            request, object_id,
            form_url,
            extra_context=extra_context
        )

    def save_formset(self, request, form, formset, change):
        """
            Set the logged in user as the medic of the medical interview.
        """
        instances = formset.save(commit=False)
        for instance in instances:
            instance.medico = request.user
            instance.save()
        formset.save_m2m()


    def queryset(self, request):
        qs = super(PatientAdmin, self).queryset(request)
        ##XXX: the fields are encrypted so this its not lazy.. must find another
        ##way
        search = request.GET.get('q', None)
        result = []
        FOUND = False
        if search:
            for elem in qs:
                if search in [elem.clinical_history, elem.name, elem.last_name, elem.dni]:
                    result.append(elem)
                    FOUND = True
            if FOUND:
                return result
        # modify queryset here, eg. only user-assigned tasks
        return qs

admin.site.register(Patient, PatientAdmin)
