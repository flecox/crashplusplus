from django.db import models
from utils import get_cie10

# Create your models here.

class Patient(models.Model):

    GENRE_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    born_date = models.DateField('Born date')
    genre = models.CharField(max_length=2,
                             choices=GENRE_CHOICES)
    dni = models.CharField(max_length=8)
    clinical_history = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    study_level =  models.IntegerField()
    social_support = models.BooleanField()


class MedicalInterview(models.Model):

    #choices for choice fields
    PF_CHOICES = [(i,i) for i in range(0, 5)]
    AIVD_CHOICES = [(i,i) for i in range(0, 31)]
    MNA_CHOICES = [(i,i) for i in range(0, 15)]
    N_COM_CAT_CHOICES = [(i,i) for i in range(1, 7)]
    CIRS_G_SEV_CHOICES = [(i,i) for i in range(0, 14)]
    CHEMO_RISK_CHOICES = [(i,i) for i in range(0, 8)]

    #fields
    date = models.DateField('Date')
    performance_status = models.CharField(max_length=2,
                                          choices=PF_CHOICES)
    cie_10 = models.CharField(max_length=4,
                              choices=get_cie10())
    initial_state = models.CharField(max_length=10)
    actual_state = models.CharField(max_length=10)
    bone_involvment = models.BooleanField()
    prior_chemotherapies = models.CharField(max_length=10)
    actual_treatment_type = models.CharField(max_length=10)
    aivd = models.CharField(max_length=4,
                           choices=AIVD_CHOICES)
    mmt = models.CharField(max_length=4,
                           choices=AIVD_CHOICES)

    mna = models.CharField(max_length=4,
                           choices=MNA_CHOICES)
    number_comorbidity_categories = models.CharField(max_length=4,
                                                     choices=N_COM_CAT_CHOICES)
    cirs_g_index = models.FloatField()
    cirs_g_severity_3 = models.CharField(max_length=4,
                                         choices=CIRS_G_SEV_CHOICES)
    falls = models.IntegerField()
    usual_medication = models.CharField(max_length=20)
    ldh = models.IntegerField()
    diatolic_blood_pressure = models.IntegerField()
    weight = models.FloatField()
    #use cm
    size = models.IntegerField()
    chemotherapy_scheme = models.CharField(max_length=30)
    chemotherapy_risk = models.CharField(max_length=30,
                                         choices=CHEMO_RISK_CHOICES)
    hematological_toxicity = models.CharField(max_length=30)
    non_hematological_toxicity = models.CharField(max_length=30)
    dose_adjustment = models.CharField(max_length=30)
    discontinuation = models.BooleanField()
    observations = models.CharField(max_length=200)

