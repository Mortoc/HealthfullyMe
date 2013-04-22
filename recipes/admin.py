from django.contrib import admin
from django.db import models
from django import forms
from django.forms.models import modelformset_factory

from recipes.models import *

class IngredientAdminInline(admin.TabularInline):
    pass

class IngredientListingAdmin(admin.ModelAdmin):
    pass

class RecipeAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)
    list_display = ('title', 'created_by', 'image_thumbnail',)
        
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(IngredientListing, IngredientListingAdmin)
admin.site.register(UnitOfMeasure)