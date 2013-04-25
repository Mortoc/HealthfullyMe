# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Recipe.featured'
        db.add_column(u'recipes_recipe', 'featured',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Recipe.featured'
        db.delete_column(u'recipes_recipe', 'featured')


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
        u'core.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'recipes.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pluralized_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'recipes.ingredientlisting': {
            'Meta': {'object_name': 'IngredientListing'},
            'amount_denominator': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'amount_numerator': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'force_pluralized': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipes.Ingredient']"}),
            'notes': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'blank': 'True'}),
            'optional': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['recipes.UnitOfMeasure']", 'null': 'True', 'blank': 'True'})
        },
        u'recipes.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'attribution': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'attribution_link': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.HMUser']"}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['recipes.RecipeImg']", 'symmetrical': 'False'}),
            'ingredient_list': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['recipes.IngredientListing']", 'symmetrical': 'False'}),
            'instructions': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'prep_time_hours': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'prep_time_minutes': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '20'}),
            'refrigeration_life_days': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'serves': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '2'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'default': 'None', 'to': u"orm['core.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'recipes.recipeimg': {
            'Meta': {'object_name': 'RecipeImg'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'recipes.unitofmeasure': {
            'Meta': {'object_name': 'UnitOfMeasure'},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'primary_key': 'True'})
        }
    }

    complete_apps = ['recipes']