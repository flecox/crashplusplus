# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User, Group
from django_extensions.db.fields.encrypted import EncryptedCharField
#change and import one by one
from vocabularies import *


class Cie10(models.Model):
    """
    This model represnt the cie-10 medical clasification for illness
    http://es.wikipedia.org/wiki/CIE-10
    """
    value = models.CharField("Valor", max_length=10)
    description = models.CharField("Descripción", max_length=100)

    def __unicode__(self):
        return self.value

    class Meta:
        verbose_name = "Cie-10"
        verbose_name_plural = "Cie-10"
        app_label = 'Pacientes'


class ChemotherapySchema(models.Model):
    """The chemotherapy scheme and its asososieted risk.
    """
    title = models.CharField("Nombre", max_length=100)
    risk = models.IntegerField("Riesgo")

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Esquema de Quimioterapia"
        verbose_name_plural = "Esquemas de Quimioterapias"
        app_label = 'Pacientes'


class Medic(models.Model):
    """
    Represents a Medic user.
    """
    user = models.OneToOneField(User)
    medic_id_number = models.CharField(max_length=100)

    def save(self, force_insert=False, force_update=False):
        try:
            group = Group.objects.get(name='Medic')
        except Group.DoesNotExist:
            # group should exist, but this is just for safety's sake,
            # it case the improbable should happen
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
        app_label = 'Pacientes'


class Patient(models.Model):

    name = EncryptedCharField("Nombre", max_length=100, )
    last_name = EncryptedCharField("Apellido", max_length=100)
    born_date = models.DateTimeField('Fecha Nacimiento', blank=True,
                                 null=True)
    genre = models.CharField("Genero", max_length=2,
                             choices=GENRE_CHOICES, blank=True,
                             null=True)
    dni = EncryptedCharField (max_length=8)
    clinical_history = EncryptedCharField ("Historia Clinica", max_length=20,
                                        blank=True, null=True)
    phone = EncryptedCharField ("Telefono", max_length=20, blank=True,
                             null=True)
    study_level = models.IntegerField("Nivel de estudio",
                                      choices=STUDY_LEVEL_CHOICES, blank=True,
                                      null=True)
    social_support = models.BooleanField("Posee Apoyo Social")

    class Meta:
        verbose_name = "Paciente"
        app_label = 'Pacientes'
        verbose_name_plural = "Pacientes"

    def __unicode__(self):
        return "%s %s - %s" % (self.name, self.last_name, self.dni)


class MedicalInterview(models.Model):
    """
    This model represent a medical interview.. in the fuure we should
    cut this big table in pieces..
    some columns are only used in the second inteview ahead.
    """

    #fields
    patient = models.ForeignKey('Patient', related_name='medical_interviews')
    medico = models.ForeignKey(User, verbose_name="Medico")
    date = models.DateField('Fecha')

    performance_status = models.IntegerField("Performance Status",
                                             choices=PF_CHOICES,
                                             blank=True, null=True)
    cie_10 = models.ForeignKey("Cie10", blank=True, null=True)
    stage = models.IntegerField("Estadio Actual", choices=CANCER_STAGE_CHOICE,
                                blank=True, null=True)
    stage_observations = models.CharField("Observaciones del estadio",
                                          max_length=100, blank=True,
                                          null=True)
    bone_compromised = models.BooleanField("Compromiso Óseo")
    prior_chemotherapies = models.CharField("Quimioterapias Anteriores",
                                            max_length=100, blank=True,
                                            null=True)
    current_treatment_type = models.IntegerField("Tipo de Tratamiento Actual",
                                                 choices=TREATMENT_TYPE_CHOICE,
                                                 blank=True, null=True)

    #aivd
    can_use_phone = models.IntegerField("¿Puede usar el teléfono?",
                                        choices=USE_PHONE_CHOICES, blank=True,
                                        null=True)

    can_walk = models.IntegerField(
        "¿Puede desplazarse a otros lugares caminando?",
        choices=USE_PHONE_CHOICES, blank=True, null=True
    )

    can_shop = models.IntegerField(
        "¿Puede ir de compras?",
        choices=USE_PHONE_CHOICES, blank=True, null=True
    )

    can_cook = models.IntegerField("¿Puede preparar su comida?",
                                   choices=USE_PHONE_CHOICES, blank=True,
                                   null=True)

    can_do_home_work = models.IntegerField(
        "¿Puede hacer las tareas del hogar?",
        choices=USE_PHONE_CHOICES,
        blank=True, null=True
    )

    can_do_manual_work = models.IntegerField("¿Puede hacer tareas manuales?",
                                             choices=USE_PHONE_CHOICES,
                                             blank=True, null=True)

    can_self_sanitize = models.IntegerField("¿Puede higienizarse?",
                                            choices=USE_PHONE_CHOICES,
                                            blank=True, null=True)

    taking_medication = models.BooleanField("¿Toma alguna medicación?")

    can_take_medication = models.IntegerField("¿Puede tomar su medicación?",
                                              choices=USE_PHONE_CHOICES,
                                              blank=True, null=True)

    can_manage_money = models.IntegerField("¿Puede manejar su dinero?",
                                           choices=USE_PHONE_CHOICES,
                                           blank=True, null=True)

    #mna
    stopped_eating = models.IntegerField(
        "¿Ha reducido la ingesta  de alimentos en los ultimos  3 meses"
        " debido  a disminución del apetito, problemas digestivos, "
        "dificultades para masticar o tragar alimentos?",
        choices=EATING_CHOICES, blank=True, null=True
    )

    lost_weight = models.IntegerField(
        "Perdida de peso en los ultimos 3 meses",
        choices=LOST_WEIGHT_CHOICES, blank=True, null=True
    )

    movility = models.IntegerField("Movilidad", choices=MOVILITY_CHOICES,
                                   blank=True, null=True)

    had_stress = models.IntegerField(
        "¿Ha sufrido stress psicologico o enfermedad aguda" +
        " en los ultimos 3 meses?",
        choices=STRESS_CHOICES, blank=True, null=True
    )

    neorologic_issues = models.IntegerField(
        "Problemas neuropsicologicos",
        choices=NEUROLOGIC_CHOICES, blank=True, null=True
    )

    #mmt
    orientation_date = models.IntegerField(
        "¿En que número y día de la semana, mes, año y estación estamos?",
        choices=[(i, i) for i in range(0, 6)], blank=True, null=True
    )

    orientation_place = models.IntegerField(
        "¿Dónde esta ud ahora? (lugar, hospital, ciudad, provincia, país)",
        choices=[(i, i) for i in range(0, 6)], blank=True, null=True
    )

    record = models.IntegerField(
        "Nombrar tres objetos lentamente. Ej: casa, zapato, papel",
        choices=[(i, i) for i in range(0, 4)], blank=True, null=True
    )

    atention_calculus = models.IntegerField(
        "múltiplos de 7 de atrás hacia adelante: 93, 86, 79, 72, 65 y" +
        "deletrear de atrás hacia adelante la palabra mundo",
        choices=[(i, i) for i in range(0, 6)], blank=True, null=True
    )

    memory = models.IntegerField(
        "Repetir los objetos nombrados anteriormente",
        choices=[(i, i) for i in range(0, 4)], blank=True, null=True
    )

    lenguage_names = models.IntegerField(
        "Mostrar un lápiz  y un reloj, preguntar sus respectivos nombres",
        choices=[(i, i) for i in range(0, 3)], blank=True, null=True
    )

    lenguage_repeat = models.IntegerField(
        "Repetir: tres perros en un trigal",
        choices=[(i, i) for i in range(0, 2)], blank=True, null=True
    )

    lenguage_indicate = models.IntegerField(
        "Indicar: tome un papel con la mano derecha, doblelo a la mitad y" +
        "pongalo en el suelo",
        choices=[(i, i) for i in range(0, 4)], blank=True, null=True
    )

    lenguage_obey = models.IntegerField(
        "Lea y obedezca lo siguiente: -CIERRE LOS OJOS-",
        choices=[(i, i) for i in range(0, 2)], blank=True, null=True
    )

    lenguage_write = models.IntegerField(
        "Escriba una oración",
        choices=[(i, i) for i in range(0, 2)], blank=True, null=True
    )

    lenguage_draw = models.IntegerField(
        "Copia de dibujo",
        choices=[(i, i) for i in range(0, 2)], blank=True, null=True
    )

    #1,2,3 y 6!!!!
    number_comorbidity_categories = models.IntegerField(
        "N° de comorbilidades",
        blank=True, null=True
    )

    cirs_g_index = models.FloatField("Indice Cirs-g", blank=True, null=True)
    cirs_g_severity_3 = models.IntegerField("Cirs-g severidad 3",
                                            choices=CIRS_G_SEV_CHOICES,
                                            blank=True, null=True)
    falls = models.IntegerField("Caidas", null=True, blank=True)
    usual_medication = models.CharField("Medicación Usual", max_length=20,
                                        blank=True, null=True)
    ldh = models.IntegerField("LDH", null=True, blank=True)
    diatolic_blood_pressure = models.IntegerField("Tensión Aterial Diastolica",
                                                  blank=True, null=True)
    sistolic_blood_pressure = models.IntegerField("Tensión Aterial Sistolica",
                                                  blank=True, null=True)
    weight = models.FloatField("Peso", blank=True, null=True)
    #use cm
    size = models.IntegerField("Talla", blank=True, null=True)
    #modelo con esquemas de quimio.
    chemotherapy_scheme = models.ForeignKey(
        "ChemotherapySchema",
        verbose_name="Esquema de Quimioterapia", blank=True, null=True
    )

    dose_adjustment = models.IntegerField(
        "Ajuste de Dosis", max_length=30,
        blank=True, null=True,
        help_text="aplica a partir de seguna entrevista"
    )
    discontinuation = models.BooleanField("Interrupción de Tratamiento")
    observations = models.CharField("Observaciones",
                                    max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.date

    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"
        app_label = 'Pacientes'
