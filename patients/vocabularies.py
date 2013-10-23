# -*- coding:utf-8 -*-

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

MOVILITY_CHOICES = (
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



#this was generated that's why its so ugly! :B
CORAZON_CHOICE = [(0, 'No hay problema'), (1, u'IAM previo(> 5 años)/ angor ocasional'), (2, u'ICC compensada con drogas/ medicación antianginosa diaria/ HVI/ FA/ bloqueo de rama/drogas antiarrítmicas diarias'), (3, u'IAM previo < 5 años/ stress test anormal/ Status pos angioplastia coronaria'), (4, u'Marcada restricción de la actividad secundaria a Status cardíaco')]
VASCULAR_CHOICE = [(0, u'No hay problema'), (1, u'HTA compensada con medidas higiénico dietéticas/ colesterol > 200 mg/dl'), (2, u'Medicación anti HTA diaria/ 1 síntoma de enfermedad ateroesclerotica ( angina, claudicación, amaurosis fugaz, ausencia de pulsos pedios )/ aneurisma de aorta > 4 cm'), (3, u'2 o más síntomas de enfermedad ateroesclerotica '), (4, u'Cirugía vascular previa/ aneurisma de aorta > 4 cm')]
HEMATOPOYETICO_CHOICE = [(0, u'No hay problema'), (1, u'Hb: mujeres > 10 <12, varones >12 < 14/ anemia de las enfermedades crónicas'), (2, u'Hb: mujeres >8 < 10, varones >10 < 12/ anemia por déficit de Fe, vit B12, ácido folico o IRC/ recuento de Globulos Blancos (GB) > 2000 pero < 4000'), (3, u'Hb: mujeres < 8, varones < 10/ GB < 2000'), (4, u'Cualquier leucemia, cualquier linfoma')]
RESPIRATORIO_CHOICE = [(0, u'No hay problema'), (1, u'Episodios recurrentes de bronquitis aguda / asma actualmente tratada con aerosoles / fumador de > 10 pero <20 pack years'), (2, u'Evidencia radiológica de EPOC / requiere teofilina o aerosoles diarios/ tratado por neumonía 2 o más veces en los últimos 5 años/ fumador de 20-40 pack years'), (3, u'Ambulacion reducida secundaria a capacidad respiratoria limitada/requiere corticoides orales para enfermedad pulmonar/ fumador de > 40 pack years'), (4, u'Requiere oxígeno suplementario/ al menos un episodio de fallo respiratorio que necesito ventilación asistida/ cualquier cáncer de pulmón')]
ORL_CHOICE = [(0, u'No hay problema'), (1, u'Visión corregida 20/40;/sinusitis crónica/hipoacusia leve'), (2, u'Visión corregida 20/60 o lee el diario con dificultad/ requiere audífono/ enfermedad sinunasal crónica que requiere medicación/ necesita medicamentos para vértigo'), (3, u'Parcialmente ciego/ incapaz de leerle diario/ audición comprometida aún con audífono'), (4, u'Ceguera funcional/ sordera funcional/ laringectomia/ requiere intervención quirúrgica para vértigo')]
GASTROINTESTINAL_SUPERIOR_CHOICE = [(0, u'No hay problema'), (1, u'Hernia de hiato/ molestias por reflujo tratadas con medicacion'), (2, u'Necesidad de anti  H2 o antiácidos diarios/ulcera gástrica o duodenal documentada dentro de los 5 años'), (3, u'Ulcera activa/ historia de ulcera perforada/ melena o hematoquecia de origen superior')]
GASTROINTESTINAL_INFERIOR_CHOICE = [(0, u'No hay problema'), (1, u'Constipación  manejada con medicación/ hemorroides activa/ status pos hernioplastia'), (2, u'Requiere laxantes diarios/ diverticulosis/ hernia no tratada'), (3, u'Oclusión intestinal en el año pasado/ uso diario de laxantes o enemas'), (4, u'Hematoquecia de origen inferior, impactación intestinal actual, diverticulitis/ status post oclusión iontestinal/ cáncer de intestino')]
HIGADO_CHOICE = [(0, u'No hay problema'), (1, u'Historia de hepatitis > 5 añosatrás/colecistectomía/ consumo cronico de alcohol en los ultimos 5 años'), (2, u'Aumento de bilirrubina total >2/ elevación de transaminasas > 150% de lo normal/ requiere enzimas pancreáticas para la digestión'), (3, u'Obstrucción biliar/ cualquier carcinoma de la vía biliar/ colecistitis/pancreatitis/ hepatitis activa')]
RENAL_CHOICE = [(0, u'No hay problema'), (1, u'Litiasis renal dentro de los últimos 10 años/ pielonefritis dentro de los últimos 5 años'), (2, u'Creatinina sérica >1,5 pero > 3 sin medicación diurética o antihipertensiva'), (3, u'Creatinina Sérica > 3 o creatinina >1,5 en conjunto con terapia diurética, antihipertensiva o bicarbonato/ pielonefritis actual'), (4, u'Requiere diálisis/ carcinoma renal')]
GENITOURINARIO_CHOICE = [(0, u'No hay problema'), (1, u'Incontinencia de orina de stress/histerectomia/ HPB asintomática'), (2, u'PAP anormal/ ITU recurrente ( 3 ó más en el pasado año)/ incontinencia de orina en mujeres/ HPB con polaquiuria/cualquierprocedimiento derivativo de via urinaria/ status pos RTU'), (3, u'Cáncer prostático in situ (incidental)/ginecorragia/ CIS de cuello uterino/hematuria/ status pos urosepsis en el pasado año'), (4, u'Retención aguda de orina/ cualquier carcinoma genitourinario ( excepto renal)')]
PIEL_Y_MUSCULOESQUELETICO_CHOICE = [(0, u'No hay problema'), (1, u'Utiliza medicación para artritis o limitación leve de las actividades de la vida diaria (AVD) por patología articular/ cáncer no melanoma de piel resecado/infecciones de piel que requirieron antibióticos en el último año '), (2, u'Medicación antiartrítica diaria, asistentes en movilidad o limitación moderada de AVD/ medicación diaria para condiciones crónicas de piel/ melanoma no metastásico'), (3, u'Compromiso severo de AVD ssecundario a artritis/requiere corticoides para enfermedad articular/ fractura vertebral con compresión por osteoporosis'), (4, u'Uso de silla de ruedas/ deformidad articular severa/osteomielitis/cualquier cancer de hueso o músculo/melanoma metastásico ')]
NEUROLOGICO_CHOICE = [(0, u'No hay problema'), (1, u'Cefaleas frecuentes que requiern medicación/ historia de AIT '), (2, u'Cefaleas crónicas que requieren medicación diaria o interfiere en las AVD/ ACV sin secuelas significativas/enfermedad neurodegenerativa leve ( Parkinson, etf'), (3, u'ACV con disfunción moderada/ cualquier procedimiento neuroquirúrgico/ enfermedad neurodegenerativa moderada'), (4, u'ACV con hemiparesia residual o afasia/enfermdad neurodegenerativa severa')]
ENDOCRINO_METABOLICO_Y_MAMA_CHOICE = [(0, u'No hay problema'), (1, u'DBT mellitus compensada con dieta/ obesidad: IMC > 30/ requiere reemplazo hormonal tiroideo'), (2, u'DBT mellitus que requiere insulina o agentes orales/ enfermedad fibroquística de la mama'), (3, u'Cualquier trastorno electrolítico que requiere hospitalización/obesidad mórbida: IMC > 45%'), (4, u'Mal control de la DBT o coma diabético en el pasado año/ requiere reemplazo hormonal adrenal// cáncer adrenal, tiroideo o de mama')]
