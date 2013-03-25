# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserAccessCode'
        db.create_table(u'core_useraccesscode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=40, db_index=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.HMUser'])),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('valid_until', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['UserAccessCode'])

        # Adding field 'HMUser.is_superuser'
        db.add_column(u'core_hmuser', 'is_superuser',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'HMUser.is_staff'
        db.add_column(u'core_hmuser', 'is_staff',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'HMUser.receives_newsletter'
        db.add_column(u'core_hmuser', 'receives_newsletter',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding M2M table for field groups on 'HMUser'
        db.create_table(u'core_hmuser_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('hmuser', models.ForeignKey(orm[u'core.hmuser'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(u'core_hmuser_groups', ['hmuser_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'HMUser'
        db.create_table(u'core_hmuser_user_permissions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('hmuser', models.ForeignKey(orm[u'core.hmuser'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(u'core_hmuser_user_permissions', ['hmuser_id', 'permission_id'])


        # Changing field 'Address.zip'
        db.alter_column(u'core_address', 'zip', self.gf('django.db.models.fields.CharField')(max_length=10))

    def backwards(self, orm):
        # Deleting model 'UserAccessCode'
        db.delete_table(u'core_useraccesscode')

        # Deleting field 'HMUser.is_superuser'
        db.delete_column(u'core_hmuser', 'is_superuser')

        # Deleting field 'HMUser.is_staff'
        db.delete_column(u'core_hmuser', 'is_staff')

        # Deleting field 'HMUser.receives_newsletter'
        db.delete_column(u'core_hmuser', 'receives_newsletter')

        # Removing M2M table for field groups on 'HMUser'
        db.delete_table('core_hmuser_groups')

        # Removing M2M table for field user_permissions on 'HMUser'
        db.delete_table('core_hmuser_user_permissions')


        # Changing field 'Address.zip'
        db.alter_column(u'core_address', 'zip', self.gf('django.db.models.fields.CharField')(max_length=8))

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
        u'core.useraccesscode': {
            'Meta': {'object_name': 'UserAccessCode'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '40', 'db_index': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.HMUser']"}),
            'valid_until': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']