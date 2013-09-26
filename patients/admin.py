from django.contrib import admin
from patients.models import Patient, MedicalInterview


class MedicalInterviewAdmin(admin.StackedInline):
	model = MedicalInterview
	extra = 1

#admin.site.register(MedicalInterview, MedicalInterviewAdmin)


class PatientAdmin(admin.ModelAdmin):
	inlines = [
        MedicalInterviewAdmin,
    ]

admin.site.register(Patient, PatientAdmin)