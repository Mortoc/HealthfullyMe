# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EmailRequest'
        db.create_table(u'home_emailrequest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'home', ['EmailRequest'])

        # Adding model 'AuthCode'
        db.create_table(u'home_authcode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.SlugField')(max_length=5)),
            ('uses_left', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'home', ['AuthCode'])

        # Adding M2M table for field registered_users on 'AuthCode'
        db.create_table(u'home_authcode_registered_users', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('authcode', models.ForeignKey(orm[u'home.authcode'], null=False)),
            ('hmuser', models.ForeignKey(orm[u'core.hmuser'], null=False))
        ))
        db.create_unique(u'home_authcode_registered_users', ['authcode_id', 'hmuser_id'])


    def backwards(self, orm):
        # Deleting model 'EmailRequest'
        db.delete_table(u'home_emailrequest')

        # Deleting model 'AuthCode'
        db.delete_table(u'home_authcode')

        # Removing M2M table for field registered_users on 'AuthCode'
        db.delete_table('home_authcode_registered_users')


    models = {
        u'core.hmuser': {
            'Meta': {'object_name': 'HMUser'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_legacy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'home.authcode': {
            'Meta': {'object_name': 'AuthCode'},
            'code': ('django.db.models.fields.SlugField', [], {'max_length': '5'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registered_users': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.HMUser']", 'symmetrical': 'False'}),
            'uses_left': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'home.emailrequest': {
            'Meta': {'object_name': 'EmailRequest'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['home']