# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Patient'
        db.create_table(u'patients_patient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('born_date', self.gf('django.db.models.fields.DateField')()),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('dni', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('clinical_history', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('study_level', self.gf('django.db.models.fields.IntegerField')()),
            ('social_support', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'patients', ['Patient'])

        # Adding model 'MedicalInterview'
        db.create_table(u'patients_medicalinterview', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(related_name='medical_interviews', to=orm['patients.Patient'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('performance_status', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('cie_10', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('initial_state', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('actual_state', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('bone_involvment', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('prior_chemotherapies', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('actual_treatment_type', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('aivd', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('mmt', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('mna', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('number_comorbidity_categories', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('cirs_g_index', self.gf('django.db.models.fields.FloatField')()),
            ('cirs_g_severity_3', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('falls', self.gf('django.db.models.fields.IntegerField')()),
            ('usual_medication', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('ldh', self.gf('django.db.models.fields.IntegerField')()),
            ('diatolic_blood_pressure', self.gf('django.db.models.fields.IntegerField')()),
            ('weight', self.gf('django.db.models.fields.FloatField')()),
            ('size', self.gf('django.db.models.fields.IntegerField')()),
            ('chemotherapy_scheme', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('chemotherapy_risk', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('hematological_toxicity', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('non_hematological_toxicity', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('dose_adjustment', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('discontinuation', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('observations', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'patients', ['MedicalInterview'])


    def backwards(self, orm):
        # Deleting model 'Patient'
        db.delete_table(u'patients_patient')

        # Deleting model 'MedicalInterview'
        db.delete_table(u'patients_medicalinterview')


    models = {
        u'patients.medicalinterview': {
            'Meta': {'object_name': 'MedicalInterview'},
            'actual_state': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'actual_treatment_type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'aivd': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'bone_involvment': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'chemotherapy_risk': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'chemotherapy_scheme': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'cie_10': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'cirs_g_index': ('django.db.models.fields.FloatField', [], {}),
            'cirs_g_severity_3': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'diatolic_blood_pressure': ('django.db.models.fields.IntegerField', [], {}),
            'discontinuation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dose_adjustment': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'falls': ('django.db.models.fields.IntegerField', [], {}),
            'hematological_toxicity': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial_state': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'ldh': ('django.db.models.fields.IntegerField', [], {}),
            'mmt': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'mna': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'non_hematological_toxicity': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'number_comorbidity_categories': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'observations': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'medical_interviews'", 'to': u"orm['patients.Patient']"}),
            'performance_status': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'prior_chemotherapies': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'size': ('django.db.models.fields.IntegerField', [], {}),
            'usual_medication': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'weight': ('django.db.models.fields.FloatField', [], {})
        },
        u'patients.patient': {
            'Meta': {'object_name': 'Patient'},
            'born_date': ('django.db.models.fields.DateField', [], {}),
            'clinical_history': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'dni': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'social_support': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'study_level': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['patients']