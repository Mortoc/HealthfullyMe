# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Giftcard'
        db.create_table('giftcards_giftcard', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('organization', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('card_id', self.gf('django.db.models.fields.BigIntegerField')()),
            ('remaining_value', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=2)),
            ('assigned_to', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('sold_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
        ))
        db.send_create_signal('giftcards', ['Giftcard'])


    def backwards(self, orm):
        # Deleting model 'Giftcard'
        db.delete_table('giftcards_giftcard')


    models = {
        'giftcards.giftcard': {
            'Meta': {'object_name': 'Giftcard'},
            'assigned_to': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            'card_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'remaining_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '2'}),
            'sold_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        }
    }

    complete_apps = ['giftcards']