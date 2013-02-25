# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'AuthCode.consumed'
        db.delete_column('home_authcode', 'consumed')

        # Adding field 'AuthCode.active'
        db.add_column('home_authcode', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'AuthCode.consumed'
        db.add_column('home_authcode', 'consumed',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'AuthCode.active'
        db.delete_column('home_authcode', 'active')


    models = {
        'home.authcode': {
            'Meta': {'object_name': 'AuthCode'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'code': ('django.db.models.fields.SlugField', [], {'max_length': '16'}),
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