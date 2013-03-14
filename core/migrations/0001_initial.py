# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Address'
        db.create_table(u'core_address', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('line1', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('line2', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2, null=True)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=64, null=True)),
        ))
        db.send_create_signal(u'core', ['Address'])


    def backwards(self, orm):
        # Deleting model 'Address'
        db.delete_table(u'core_address')


    models = {
        u'core.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'line1': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'line2': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        }
    }

    complete_apps = ['core']