# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'EmailRequest.code_sent'
        db.add_column(u'home_emailrequest', 'code_sent',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'EmailRequest.code_sent'
        db.delete_column(u'home_emailrequest', 'code_sent')


    models = {
        u'core.hmuser': {
            'Meta': {'object_name': 'HMUser'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_legacy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'}),
            'logins': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.LoginInfo']", 'symmetrical': 'False'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'receives_newsletter': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'core.logininfo': {
            'Meta': {'object_name': 'LoginInfo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.HMUser']", 'null': 'True'})
        },
        u'home.authcode': {
            'Meta': {'object_name': 'AuthCode'},
            'code': ('django.db.models.fields.SlugField', [], {'max_length': '5'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'default': "' '"}),
            'registered_users': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.HMUser']", 'symmetrical': 'False'}),
            'uses_left': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'home.emailrequest': {
            'Meta': {'object_name': 'EmailRequest'},
            'code_sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'code_sent_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['home']