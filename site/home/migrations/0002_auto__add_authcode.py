# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AuthCode'
        db.create_table('home_authcode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.SlugField')(max_length=16)),
            ('consumed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 2, 21, 0, 0))),
        ))
        db.send_create_signal('home', ['AuthCode'])


    def backwards(self, orm):
        # Deleting model 'AuthCode'
        db.delete_table('home_authcode')


    models = {
        'home.authcode': {
            'Meta': {'object_name': 'AuthCode'},
            'code': ('django.db.models.fields.SlugField', [], {'max_length': '16'}),
            'consumed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 21, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'home.emailrequest': {
            'Meta': {'object_name': 'EmailRequest'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 21, 0, 0)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['home']