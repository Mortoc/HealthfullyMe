# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Offer.fulfillment'
        db.add_column(u'store_offer', 'fulfillment',
                      self.gf('django.db.models.fields.CharField')(default='MAN', max_length=3),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Offer.fulfillment'
        db.delete_column(u'store_offer', 'fulfillment')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'line1': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'line2': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'core.hmuser': {
            'Meta': {'object_name': 'HMUser'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_legacy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'}),
            'logins': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.LoginInfo']", 'symmetrical': 'False'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'receives_newsletter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'core.logininfo': {
            'Meta': {'object_name': 'LoginInfo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.HMUser']", 'null': 'True'})
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
            'availability': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['store.OfferAvailability']", 'null': 'True', 'blank': 'True'}),
            'buy_window_description': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'buy_window_title': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'description_line_1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '96', 'null': 'True', 'blank': 'True'}),
            'description_line_2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '96', 'null': 'True', 'blank': 'True'}),
            'description_line_3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '96', 'null': 'True', 'blank': 'True'}),
            'description_line_4': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '96', 'null': 'True', 'blank': 'True'}),
            'description_line_5': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '96', 'null': 'True', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fulfillment': ('django.db.models.fields.CharField', [], {'default': "'MAN'", 'max_length': '3'}),
            'header_text': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'default': "'/static/img/product/wholefoods.jpg'", 'max_length': '128'}),
            'price': ('django.db.models.fields.IntegerField', [], {'default': '4000'}),
            'thumbnail_image': ('django.db.models.fields.CharField', [], {'default': "'/static/img/product/wholefoods128.png'", 'max_length': '128'})
        },
        u'store.offeravailability': {
            'Meta': {'object_name': 'OfferAvailability'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'purchases': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'time_peroid': ('django.db.models.fields.SmallIntegerField', [], {}),
            'time_value': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'store.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'card': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['store.Card']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_slug': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'offer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['store.Offer']"}),
            'shipped': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'shipping_tracking_data': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'stripe_id': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.HMUser']"})
        }
    }

    complete_apps = ['store']