
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

TREATMENT_TYPE_CHOICE = (
    (0, 'adyuvante'),
    (1, 'neoadyuvante'),
    (2, 'Primera linea avanzado'),
    (3, 'Segunda linea avanzado'),
    (4, 'Tercera linea avanzado'),
    (5, 'Cuarta linea avanzado'),
    (5, 'Multiples lineas'),
)

#choices for choice fields
PF_CHOICES = [(i, i) for i in range(0, 6)]

CANCER_STAGE_CHOICE = (
    (0, "0"),
    (1, "I"),
    (2, "II"),
    (3, "III"),
    (4, "IV"),
)

AIVD_CHOICES = [(i, i) for i in range(0, 31)]
MNA_CHOICES = [(i, i) for i in range(0, 15)]
N_COM_CAT_CHOICES = [(i, i) for i in range(1, 7)]
CIRS_G_SEV_CHOICES = [(i, i) for i in range(0, 14)]
CHEMO_RISK_CHOICES = [(i, i) for i in range(0, 8)]
USE_PHONE_CHOICES = (
    (3, "Sin ayuda"),
    (2, "Con cierta ayuda"),
    (1, "Es completamente incapaz")
)

EATING_CHOICES = (
    (0, "Disminución severa"),
    (1, "Disminución moderada"),
    (2, "No ha disminuido"),
)

LOST_WEIGHT_CHOICES = (
    (0, "> 3kg"),
    (1, "No sabe"),
    (2, "Entre 1 y 3 kh"),
    (3, "No ha perdido peso"),
)

MOVILITY_CHOICES =  (
    (0, "Permanece en cama"),
    (1, "Capaz de salir de la cama o silla pero no fuera de la casa"),
    (2, "Sale de la casa"),
)

STRESS_CHOICES = (
    (0, 'Si'),
    (1, 'No'),
)

NEUROLOGIC_CHOICES = (
    (0, "Demencia severa o depresión"),
    (1, "Demencia leve"),
    (2, "Sin problemas")
)
