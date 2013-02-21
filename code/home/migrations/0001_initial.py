# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EmailRequest'
        db.create_table('home_emailrequest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 2, 19, 0, 0))),
        ))
        db.send_create_signal('home', ['EmailRequest'])


    def backwards(self, orm):
        # Deleting model 'EmailRequest'
        db.delete_table('home_emailrequest')


    models = {
        'home.emailrequest': {
            'Meta': {'object_name': 'EmailRequest'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['home']