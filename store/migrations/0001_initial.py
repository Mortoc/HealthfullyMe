# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ComingSoonIdea'
        db.create_table(u'store_comingsoonidea', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=160)),
            ('times_shown', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('times_selected', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'store', ['ComingSoonIdea'])

        # Adding model 'Offer'
        db.create_table(u'store_offer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('header_text', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('description_line_1', self.gf('django.db.models.fields.CharField')(default='', max_length=96, null=True, blank=True)),
            ('description_line_2', self.gf('django.db.models.fields.CharField')(default='', max_length=96, null=True, blank=True)),
            ('description_line_3', self.gf('django.db.models.fields.CharField')(default='', max_length=96, null=True, blank=True)),
            ('description_line_4', self.gf('django.db.models.fields.CharField')(default='', max_length=96, null=True, blank=True)),
            ('description_line_5', self.gf('django.db.models.fields.CharField')(default='', max_length=96, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.CharField')(default='/static/img/product/wholefoods.jpg', max_length=128)),
            ('thumbnail_image', self.gf('django.db.models.fields.CharField')(default='/static/img/product/wholefoods128.png', max_length=128)),
            ('buy_window_title', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('buy_window_description', self.gf('django.db.models.fields.CharField')(max_length=64, null=True)),
            ('price', self.gf('django.db.models.fields.IntegerField')(default=4000)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'store', ['Offer'])

        # Adding model 'Card'
        db.create_table(u'store_card', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.HMUser'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('fingerprint', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last4', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['core.Address'], null=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('expire_month', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('expire_year', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'store', ['Card'])

        # Adding model 'Transaction'
        db.create_table(u'store_transaction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('id_slug', self.gf('django.db.models.fields.CharField')(default='', max_length=16)),
            ('offer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['store.Offer'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.HMUser'])),
            ('card', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['store.Card'], null=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'store', ['Transaction'])


    def backwards(self, orm):
        # Deleting model 'ComingSoonIdea'
        db.delete_table(u'store_comingsoonidea')

        # Deleting model 'Offer'
        db.delete_table(u'store_offer')

        # Deleting model 'Card'
        db.delete_table(u'store_card')

        # Deleting model 'Transaction'
        db.delete_table(u'store_transaction')


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
        },
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
        u'store.card': {
            'Meta': {'object_name': 'Card'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['core.Address']", 'null': 'True'}),
            'expire_month': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'expire_year': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'fingerprint': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last4': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.HMUser']"})
        },
        u'store.comingsoonidea': {
            'Meta': {'object_name': 'ComingSoonIdea'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'times_selected': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'times_shown': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'store.offer': {
            'Meta': {'object_name': 'Offer'},
            'buy_window_description': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'buy_window_title': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'description_line_1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '96', 'null': 'True', 'blank': 'True'}),
            'description_line_2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '96', 'null': 'True', 'blank': 'True'}),
            'description_line_3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '96', 'null': 'True', 'blank': 'True'}),
            'description_line_4': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '96', 'null': 'True', 'blank': 'True'}),
            'description_line_5': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '96', 'null': 'True', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'header_text': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'default': "'/static/img/product/wholefoods.jpg'", 'max_length': '128'}),
            'price': ('django.db.models.fields.IntegerField', [], {'default': '4000'}),
            'thumbnail_image': ('django.db.models.fields.CharField', [], {'default': "'/static/img/product/wholefoods128.png'", 'max_length': '128'})
        },
        u'store.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'card': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['store.Card']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_slug': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '16'}),
            'offer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['store.Offer']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.HMUser']"})
        }
    }

    complete_apps = ['store']