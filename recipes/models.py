from django.db import models
from django.utils.timezone import now
from django.conf import settings
from django.utils.safestring import mark_safe 

from core.models import HMUser, Tag

import random

class UnitOfMeasure(models.Model):
    name = models.CharField(primary_key=True, max_length=32)
    
    def __unicode__(self):
        return self.name
        
        
class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    pluralized_name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.name
    
class IngredientListing(models.Model):
    id = models.AutoField(primary_key=True)
    amount_numerator = models.PositiveSmallIntegerField(default=1)
    amount_denominator = models.PositiveSmallIntegerField(default=1)
    unit = models.ForeignKey( UnitOfMeasure, null=True, blank=True, default=None )
    ingredient = models.ForeignKey( Ingredient )
    notes = models.CharField( max_length=255, blank=True, default=None )
    optional = models.BooleanField( default=False )
    force_pluralized = models.BooleanField( default=False )

    def __unicode__(self):
        number = ""
        
        # Format the fraction nicely
        if self.amount_numerator > 0 and self.amount_denominator > 0:
            # 3/1 Cups should read '3 Cups'
            if self.amount_denominator == 1:
                number = self.amount_numerator
                
            # 3/2 Cups should read '1 1/2 Cups'
            elif self.amount_numerator > self.amount_denominator:
                integer = self.amount_numerator / self.amount_denominator;
                remainder = self.amount_numerator % self.amount_denominator;
                
                if remainder == 0:
                    number = "{0}".format( integer )
                else:
                    number = "{0} {1}/{2}".format( integer, remainder, self.amount_denominator )
                
            # 1/2 Cups should read '1/2 Cups'
            else:
                number = "{0}/{1}".format( self.amount_numerator, self.amount_denominator )
        
        unit = ""
        if self.unit:
            unit = "{0} ".format(self.unit)
        
        optional = ""
        if self.optional:
            optional = " (Optional)"
        
        notes = ""
        if self.notes:
            notes = " " + self.notes
            
        # Ingredient.name or Ingredient.pluralized_name
        ingredient = ""
        if self.force_pluralized or (self.amount_numerator != 0 and self.amount_numerator != self.amount_denominator):
            ingredient = self.ingredient.pluralized_name
        else:
            ingredient = self.ingredient.name
            
        return u"{0} {1}{2}{3}{4}".format( number, unit, ingredient, notes, optional )
        
class RecipeImg(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.url
    
class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    
    title = models.CharField(max_length=128)
    images = models.ManyToManyField(RecipeImg)
    tags = models.ManyToManyField(Tag, blank=True, default=None)
    ingredient_list = models.ManyToManyField(IngredientListing)
    instructions = models.TextField(default="")
    
    attribution = models.CharField(max_length=64, null=True, blank=True)
    attribution_link = models.CharField(max_length=512, null=True, blank=True)
    
    created_by = models.ForeignKey(HMUser)
    created_date = models.DateTimeField(default=now)
    
    serves = models.PositiveSmallIntegerField(default=2)
    prep_time_hours = models.PositiveSmallIntegerField(default=0)
    prep_time_minutes = models.PositiveSmallIntegerField(default=20)
    
    refrigeration_life_days = models.PositiveSmallIntegerField(blank=True, null=True, default=None)
    
    featured = models.BooleanField(default=False)
    
    def prep_time_formatted(self):
        result = u""
        if self.prep_time_hours > 0:
            hours_plural = "s" if self.prep_time_hours > 1 else ""
            result = u"{0} hour{1}".format(self.prep_time_hours, hours_plural)
            
        if self.prep_time_minutes > 0:
            comma = ", " if self.prep_time_hours > 0 else ""
            min_plural = "s" if self.prep_time_minutes > 0 else ""
            result = u"{0}{1}{2} minute{3}".format(result, comma, self.prep_time_minutes, min_plural)
        
        if self.prep_time_minutes == 0 and self.prep_time_hours == 0:
            result = "Instant"                
        return result;
        

    def thumbnail_url(self):
        img_url = ""
        
        images = list(self.images.all())
        img_len = len(images)
        if img_len > 0:
            img_url = images[random.randint(0, img_len - 1)].url
            
        return img_url
            
    def image_thumbnail(self):
        return u"<img src=\"{0}\" height=\"64px\"></img>".format( self.thumbnail_url() )
    image_thumbnail.short_description = 'Thumb'
    image_thumbnail.allow_tags = True
    
    
    def __unicode__(self):
        return self.title
        
    def get_instructions_html(self):
        return mark_safe(self.instructions)
        
    get_instructions_html.allow_tags = True
        
        