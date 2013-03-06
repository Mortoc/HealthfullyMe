# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Card.address_state'
        db.delete_column('store_card', 'address_state')

        # Deleting field 'Card.address_country'
        db.delete_column('store_card', 'address_country')

        # Deleting field 'Card.address_zip'
        db.delete_column('store_card', 'address_zip')

        # Deleting field 'Card.address_line2'
        db.delete_column('store_card', 'address_line2')

        # Deleting field 'Card.address_city'
        db.delete_column('store_card', 'address_city')

        # Deleting field 'Card.address_line1'
        db.delete_column('store_card', 'address_line1')

        # Adding field 'Card.address'
        db.add_column('store_card', 'address',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['core.Address'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Card.address_state'
        db.add_column('store_card', 'address_state',
                      self.gf('django.db.models.fields.CharField')(max_length=2, null=True),
                      keep_default=False)

        # Adding field 'Card.address_country'
        db.add_column('store_card', 'address_country',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True),
                      keep_default=False)

        # Adding field 'Card.address_zip'
        db.add_column('store_card', 'address_zip',
                      self.gf('django.db.models.fields.CharField')(default='None', max_length=8),
                      keep_default=False)

        # Adding field 'Card.address_line2'
        db.add_column('store_card', 'address_line2',
                      self.gf('django.db.models.fields.CharField')(max_length=256, null=True),
                      keep_default=False)

        # Adding field 'Card.address_city'
        db.add_column('store_card', 'address_city',
                      self.gf('django.db.models.fields.CharField')(max_length=256, null=True),
                      keep_default=False)

        # Adding field 'Card.address_line1'
        db.add_column('store_card', 'address_line1',
                      self.gf('django.db.models.fields.CharField')(default='unused', max_length=256),
                      keep_default=False)

        # Deleting field 'Card.address'
        db.delete_column('store_card', 'address_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.address': {
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
        'store.card': {
            'Meta': {'object_name': 'Card'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['core.Address']", 'null': 'True'}),
            'expire_month': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'expire_year': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'fingerprint': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last4': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'store.comingsoonidea': {
            'Meta': {'object_name': 'ComingSoonIdea'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'times_selected': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'times_shown': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'store.offer': {
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
        'store.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'card': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['store.Card']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_slug': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '16'}),
            'offer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['store.Offer']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['store']