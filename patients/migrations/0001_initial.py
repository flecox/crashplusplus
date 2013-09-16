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


    def backwards(self, orm):
        # Deleting model 'Patient'
        db.delete_table(u'patients_patient')


    models = {
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