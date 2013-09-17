from django.contrib import admin
from patients.models import Patient, MedicalInterview

class PatientAdmin(admin.ModelAdmin):
    pass

admin.site.register(Patient, PatientAdmin)

class MedicalInterviewAdmin(admin.ModelAdmin):
    pass

admin.site.register(MedicalInterview, MedicalInterviewAdmin)