# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

class Cie10(models.Model):
    value = models.CharField("Valor", max_length=10)
    description = models.CharField("Descripción", max_length=100)

    def __unicode__(self):
        return self.value

    class Meta:
        verbose_name = "Cie-10"
        verbose_name_plural = "Cie-10"


class ChemotherapySchema(models.Model):
    title = models.CharField("Nombre", max_length=100)
    risk = models.IntegerField("Riesgo")

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Esquema de Quimioterapia"
        verbose_name_plural = "Esquemas de Quimioterapias"


class Medic(models.Model):
    user = models.OneToOneField(User)
    medic_id_number = models.CharField(max_length=100)

    def save(self, force_insert=False, force_update=False):
        try:
            group = Group.objects.get(name='Medic')
        except Group.DoesNotExist:
            # group should exist, but this is just for safety's sake, it case the improbable should happen
            pass
        else:
            self.user.groups.add(group)
        self.user.is_staff = True
        self.user.save()
        super(Medic, self).save(force_insert, force_update)

    def __unicode__(self):
        return "%s-%s" % (self.user.username, self.medic_id_number)

    class Meta:
        verbose_name = "Medico"
        verbose_name_plural = "Medicos"


class Patient(models.Model):

    GENRE_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )

    STUDY_LEVEL_CHOICES = (
        (1, 'Primaria Incompleta'),
        (2, 'Primaria Completa'),
        (3, 'Secundaria Incompleta'),
        (4, 'Secundaria Completa'),
        (5, 'Universidad Completa'),
        (6, 'Universidad Incompleta'),
    )

    name = models.CharField("Nombre", max_length=100, )
    last_name = models.CharField("Apellido", max_length=100)
    born_date = models.DateField('Fecha Nacimiento')
    genre = models.CharField("Genero", max_length=2,
                             choices=GENRE_CHOICES)
    dni = models.CharField(max_length=8)
    clinical_history = models.CharField("Historia Clinica", max_length=20)
    phone = models.CharField("Telefono", max_length=20)
    study_level =  models.IntegerField("Nivel de estudio", choices=STUDY_LEVEL_CHOICES)
    social_support = models.BooleanField("Apoyo Social")

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __unicode__(self):
        return "%s %s - %s" % (self.name, self.last_name, self.dni)


class MedicalInterview(models.Model):


    TREATMENT_TYPE_CHOICE = (
        (0, 'adyuvante'),
        (1, 'neoadyuvante'),
        (2, 'First line advanced'),
        (3, 'Second line advanced'),
        (4, 'Third line advanced'),
        (5, 'Four line advanced'),
    )


    #choices for choice fields
    PF_CHOICES = (
        (0, "ECOG0: Vida Normal"),
        (1, "ECOG1: no puede hacer trabajo duro"),
        (2, "ECOG2: <50% en cama"),
        (3, "ECOG3: >50% en cama"),
        (4, "ECOG4: 100% en cama"),
        (5, "ECOG5: Fallecido"),
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
    medico = models.ForeignKey('Medic', verbose_name="Medico")
    date = models.DateField('Fecha')

    performance_status = models.IntegerField("Estado Funcional",choices=PF_CHOICES, blank=True, null=True)
    cie_10 = models.ForeignKey("Cie10")
    initial_stage = models.IntegerField("Estado Inicial",choices=CANCER_STAGE_CHOICE)
    current_stage = models.IntegerField("Estado Actual", choices=CANCER_STAGE_CHOICE)
    bone_compromised = models.BooleanField("Compromiso Óseo")
    prior_chemotherapies = models.CharField("Quimioterapias Anteriores", max_length=10, blank=True, null=True)
    current_treatment_type = models.IntegerField("Tipo de Tratamiento Actual", choices=TREATMENT_TYPE_CHOICE)
    aivd = models.IntegerField("Aivd", choices=AIVD_CHOICES, blank=True, null=True)
    mmt = models.IntegerField("Mmt", choices=AIVD_CHOICES, blank=True, null=True)

    mna = models.IntegerField("Mna",choices=MNA_CHOICES, blank=True, null=True)
    #1,2,3 y 6!!!!
    number_comorbidity_categories = models.IntegerField("N° de categorias de comorbilidades",choices=N_COM_CAT_CHOICES, blank=True, null=True)

    cirs_g_index = models.FloatField("Indice Cirs-g", blank=True, null=True)
    cirs_g_severity_3 = models.IntegerField("Cirs-g severidad 3", choices=CIRS_G_SEV_CHOICES, blank=True, null=True)
    falls = models.IntegerField("Caidas", null=True, blank=True)
    usual_medication = models.CharField("Medicación Usual", max_length=20, blank=True, null=True)
    ldh = models.IntegerField("LDH", null=True, blank=True)
    diatolic_blood_pressure = models.IntegerField("Tensión Aterial Diastolica", blank=True, null=True)
    weight = models.FloatField("Peso", blank=True, null=True)
    #use cm
    size = models.IntegerField("Talla", blank=True, null=True)
    #modelo con esquemas de quimio.
    chemotherapy_scheme = models.ForeignKey("ChemotherapySchema", verbose_name="Esquema de Quimioterapia")


    chemotherapy_risk = models.IntegerField("Riesgo de Quimioterapia", choices=CHEMO_RISK_CHOICES, blank=True, null=True)
    dose_adjustment = models.CharField("Ajuste de Dosis", max_length=30, blank=True, null=True)
    discontinuation = models.BooleanField("Interrupción de Tratamiento")
    observations = models.CharField("Observaciones", max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.date

    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"
