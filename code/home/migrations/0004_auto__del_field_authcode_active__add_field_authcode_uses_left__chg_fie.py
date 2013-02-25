# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'AuthCode.active'
        db.delete_column('home_authcode', 'active')

        # Adding field 'AuthCode.uses_left'
        db.add_column('home_authcode', 'uses_left',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


        # Changing field 'AuthCode.code'
        db.alter_column('home_authcode', 'code', self.gf('django.db.models.fields.SlugField')(max_length=5))

    def backwards(self, orm):
        # Adding field 'AuthCode.active'
        db.add_column('home_authcode', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Deleting field 'AuthCode.uses_left'
        db.delete_column('home_authcode', 'uses_left')


        # Changing field 'AuthCode.code'
        db.alter_column('home_authcode', 'code', self.gf('django.db.models.fields.SlugField')(max_length=16))

    models = {
        'home.authcode': {
            'Meta': {'object_name': 'AuthCode'},
            'code': ('django.db.models.fields.SlugField', [], {'max_length': '5'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 21, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uses_left': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'home.emailrequest': {
            'Meta': {'object_name': 'EmailRequest'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 21, 0, 0)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['home']