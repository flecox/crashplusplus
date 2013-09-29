from django.db import models
from utils import get_cie10
import eav

# Create your models here.

class Patient(models.Model):

    GENRE_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    STUDY_LEVEL_CHOICES = (
        (1, 'Elementary Incomplete'),
        (2, 'Elementary Complete'),
        (3, 'High School Incomplete'),
        (4, 'High School Complete'),
        (5, 'Univeristy Incomplete'),
        (6, 'University Complete'),
    )

    name = models.CharField(max_length=100, )
    last_name = models.CharField(max_length=100)
    born_date = models.DateField('Born date')
    genre = models.CharField(max_length=2,
                             choices=GENRE_CHOICES)
    dni = models.CharField(max_length=8)
    clinical_history = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    study_level =  models.IntegerField(choices=STUDY_LEVEL_CHOICES)
    social_support = models.BooleanField()

    def __unicode__(self):
        return "%s %s - %s" % (self.name, self.last_name, self.dni)


class MedicalInterview(models.Model):

    #choices for choice fields
    PF_CHOICES = (
        (0, "ECOG0: Normal Life"),
        (1, "ECOG1: unable to do hard work"),
        (2, "ECOG2: <50% in bed"),
        (3, "ECOG3: >50% in bed"),
        (4, "ECOG4: 100% in bed"),
        (5, "ECOG5: Dead"),
    )

    CANCER_STAGE_CHOICE = (
        (0, "0"),
        (1, "I"),
        (2, "II"),
        (3, "III"),
        (4, "IV"),
    )
    AIVD_CHOICES = [(i,i) for i in range(0, 31)]
    MNA_CHOICES = [(i,i) for i in range(0, 15)]
    N_COM_CAT_CHOICES = [(i,i) for i in range(1, 7)]
    CIRS_G_SEV_CHOICES = [(i,i) for i in range(0, 14)]
    CHEMO_RISK_CHOICES = [(i,i) for i in range(0, 8)]

    #fields
    patient = models.ForeignKey('Patient', related_name='medical_interviews')
    date = models.DateField('Date')

    performance_status = models.IntegerField(choices=PF_CHOICES, blank=True, null=True)
    cie_10 = models.CharField(max_length=4,#auto completado desde la base
                              choices=get_cie10(), blank=True, null=True)
    initial_stage = models.IntegerField(choices=CANCER_STAGE_CHOICE)
    current_stage = models.IntegerField(choices=CANCER_STAGE_CHOICE)
    bone_compromised = models.BooleanField()
    prior_chemotherapies = models.CharField(max_length=10, blank=True, null=True)
    current_treatment_type = models.CharField(max_length=10, blank=True, null=True)
    aivd = models.IntegerField(choices=AIVD_CHOICES, blank=True, null=True)
    mmt = models.IntegerField(choices=AIVD_CHOICES, blank=True, null=True)

    mna = models.IntegerField(choices=MNA_CHOICES, blank=True, null=True)
    #1,2,3 y 6!!!!
    number_comorbidity_categories = models.IntegerField(choices=N_COM_CAT_CHOICES, blank=True, null=True)

    cirs_g_index = models.FloatField(blank=True, null=True)
    cirs_g_severity_3 = models.IntegerField(choices=CIRS_G_SEV_CHOICES, blank=True, null=True)
    falls = models.IntegerField(null=True, blank=True)
    usual_medication = models.CharField(max_length=20, blank=True, null=True)
    ldh = models.IntegerField(null=True, blank=True)
    diatolic_blood_pressure = models.IntegerField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    #use cm
    size = models.IntegerField(blank=True, null=True)
    #modelo con esquemas de quimio.
    chemotherapy_scheme = models.CharField(max_length=30, blank=True, null=True)
    chemotherapy_risk = models.IntegerField(choices=CHEMO_RISK_CHOICES, blank=True, null=True)
    dose_adjustment = models.CharField(max_length=30, blank=True, null=True)
    discontinuation = models.BooleanField()
    observations = models.CharField(max_length=200, blank=True, null=True)


eav.register(MedicalInterview)
