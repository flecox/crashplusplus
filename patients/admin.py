from django.contrib import admin
from patients.models import Patient, MedicalInterview


class MedicalInterviewAdmin(admin.TabularInline):
	model = MedicalInterview

#admin.site.register(MedicalInterview, MedicalInterviewAdmin)


class PatientAdmin(admin.ModelAdmin):
	inlines = [
        MedicalInterviewAdmin,
    ]

admin.site.register(Patient, PatientAdmin)