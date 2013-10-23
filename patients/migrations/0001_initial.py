# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cie10'
        db.create_table(u'patients_cie10', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'patients', ['Cie10'])

        # Adding model 'ChemotherapySchema'
        db.create_table(u'patients_chemotherapyschema', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('risk', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'patients', ['ChemotherapySchema'])

        # Adding model 'Medic'
        db.create_table(u'patients_medic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('medic_id_number', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'patients', ['Medic'])

        # Adding model 'Patient'
        db.create_table(u'patients_patient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=214)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=214)),
            ('born_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('dni', self.gf('django.db.models.fields.CharField')(max_length=86)),
            ('clinical_history', self.gf('django.db.models.fields.CharField')(max_length=108, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=108, null=True, blank=True)),
            ('study_level', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('social_support', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'patients', ['Patient'])

        # Adding model 'MedicalInterview'
        db.create_table(u'patients_medicalinterview', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(related_name='medical_interviews', to=orm['patients.Patient'])),
            ('medico', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('performance_status', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cie_10', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patients.Cie10'], null=True, blank=True)),
            ('stage', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('stage_observations', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('bone_compromised', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('prior_chemotherapies', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('current_treatment_type', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('corazon', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('vascular', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('hematopoyetico', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('respiratorio', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('orl', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('gastrointestinal_superior', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('gastrointestinal_inferior', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('higado', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('renal', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('genitourinario', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('piel_y_musculoesqueletico', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('neurologico', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('endocrino_metabolico_y_mama', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('enfermedad_psiquiatrica', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('can_use_phone', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('can_walk', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('can_shop', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('can_cook', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('can_do_home_work', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('can_do_manual_work', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('can_self_sanitize', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('taking_medication', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('can_take_medication', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('can_manage_money', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('stopped_eating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('lost_weight', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('movility', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('had_stress', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('neorologic_issues', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('orientation_date', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('orientation_place', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('record', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('atention_calculus', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('memory', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('lenguage_names', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('lenguage_repeat', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('lenguage_indicate', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('lenguage_obey', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('lenguage_write', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('lenguage_draw', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('number_comorbidity_categories', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cirs_g_index', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('cirs_g_severity_3', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('falls', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('usual_medication', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('ldh', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('diatolic_blood_pressure', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sistolic_blood_pressure', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('size', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('chemotherapy_scheme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patients.ChemotherapySchema'], null=True, blank=True)),
            ('dose_adjustment', self.gf('django.db.models.fields.IntegerField')(max_length=30, null=True, blank=True)),
            ('discontinuation', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('observations', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'patients', ['MedicalInterview'])


    def backwards(self, orm):
        # Deleting model 'Cie10'
        db.delete_table(u'patients_cie10')

        # Deleting model 'ChemotherapySchema'
        db.delete_table(u'patients_chemotherapyschema')

        # Deleting model 'Medic'
        db.delete_table(u'patients_medic')

        # Deleting model 'Patient'
        db.delete_table(u'patients_patient')

        # Deleting model 'MedicalInterview'
        db.delete_table(u'patients_medicalinterview')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'patients.chemotherapyschema': {
            'Meta': {'object_name': 'ChemotherapySchema'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'risk': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'patients.cie10': {
            'Meta': {'object_name': 'Cie10'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'patients.medic': {
            'Meta': {'object_name': 'Medic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medic_id_number': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'patients.medicalinterview': {
            'Meta': {'object_name': 'MedicalInterview'},
            'atention_calculus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'bone_compromised': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'can_cook': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'can_do_home_work': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'can_do_manual_work': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'can_manage_money': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'can_self_sanitize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'can_shop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'can_take_medication': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'can_use_phone': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'can_walk': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'chemotherapy_scheme': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patients.ChemotherapySchema']", 'null': 'True', 'blank': 'True'}),
            'cie_10': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patients.Cie10']", 'null': 'True', 'blank': 'True'}),
            'cirs_g_index': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cirs_g_severity_3': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'corazon': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'current_treatment_type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'diatolic_blood_pressure': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'discontinuation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dose_adjustment': ('django.db.models.fields.IntegerField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'endocrino_metabolico_y_mama': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'enfermedad_psiquiatrica': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'falls': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gastrointestinal_inferior': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gastrointestinal_superior': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'genitourinario': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'had_stress': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hematopoyetico': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'higado': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ldh': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'lenguage_draw': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'lenguage_indicate': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'lenguage_names': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'lenguage_obey': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'lenguage_repeat': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'lenguage_write': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'lost_weight': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'medico': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'memory': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'movility': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'neorologic_issues': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'neurologico': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'number_comorbidity_categories': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'observations': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'orientation_date': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'orientation_place': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'orl': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'medical_interviews'", 'to': u"orm['patients.Patient']"}),
            'performance_status': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'piel_y_musculoesqueletico': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'prior_chemotherapies': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'record': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'renal': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'respiratorio': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sistolic_blood_pressure': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'stage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'stage_observations': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'stopped_eating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'taking_medication': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'usual_medication': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'vascular': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'patients.patient': {
            'Meta': {'object_name': 'Patient'},
            'born_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'clinical_history': ('django.db.models.fields.CharField', [], {'max_length': '108', 'null': 'True', 'blank': 'True'}),
            'dni': ('django.db.models.fields.CharField', [], {'max_length': '86'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '214'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '214'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '108', 'null': 'True', 'blank': 'True'}),
            'social_support': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'study_level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['patients']