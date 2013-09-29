from django.contrib import admin
from patients.models import Patient, MedicalInterview, Medic
from eav.admin import BaseEntityInline
from eav.forms import BaseDynamicEntityForm

class MedicAdmin(admin.ModelAdmin):
    pass

admin.site.register(Medic, MedicAdmin)


class MedicalForm(BaseDynamicEntityForm):
    class Meta:
        model = MedicalInterview


class MedicalInterviewAdmin(BaseEntityInline, admin.StackedInline):
    model = MedicalInterview
    form = MedicalForm
    extra = 0
    # fieldsets = (
    #     (None, {
    #         'fields': ('date', ),
    #     }),
    #     ("interview Data", {'fields': ('performance_status', 'cie_10', 'initial_stage',
    #         'current_stage', 'bone_compromised', 'prior_chemotherapies',
    #         'current_treatment_type', 'aivd', 'mmt', 'mna',
    #         'number_comorbidity_categories', 'cirs_g_index', 'cirs_g_severity_3',
    #         'falls', 'usual_medication', 'ldh', 'diatolic_blood_pressure',
    #         'weight', 'size', 'chemotherapy_scheme', 'chemotherapy_risk',
    #         'dose_adjustment', 'discontinuation', 'observations'),
    #         'classes': ("collapse",)})
    # )

    # def get_readonly_fields(self, request, obj=None):
    #     if 'edit' not in request.GET and len(self.queryset(request)) > 0:
    #         return ('date',)
    #     else:
    #         return self.readonly_fields

#admin.site.register(MedicalInterview, MedicalInterviewAdmin)


class PatientAdmin(admin.ModelAdmin):
    list_display_links = ('name', 'last_name')
    list_display = ('name', 'last_name', 'clinical_history', 'dni')

    inlines = [
        MedicalInterviewAdmin,
    ]

    fieldsets = (
        ('Patient Data', {
            'fields': (('name', 'last_name'), ('dni', 'clinical_history'),
                        'born_date', 'genre', 'phone' ),
        }),
        (None, {
            'fields': (('study_level', 'social_support'), ),
        })
    )

    search_fields = ['name', 'last_name','dni', 'clinical_history']

    def get_readonly_fields(self, request, obj=None):
        if 'edit' not in request.GET:
            return ('name', 'last_name', 'born_date', 'genre', 'dni',
                    'clinical_history', 'phone', 'study_level', 'social_support')
        else:
            return self.readonly_fields

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['add'] = False
        # or
        extra_context['show_save'] = False
        extra_context['show_save_continue'] = False
        extra_context['show_save_continue'] = False
        extra_context['show_save_add'] = False
        return super(PatientAdmin, self).change_view(request, object_id,
            form_url, extra_context=extra_context)

admin.site.register(Patient, PatientAdmin)