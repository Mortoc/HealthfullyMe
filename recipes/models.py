from django.db import models
from django.utils.timezone import now
from django.conf import settings

from core.models import HMUser, Tag

class UnitOfMeasure(models.Model):
    name = models.CharField(primary_key=True, max_length=32)
    
    def __unicode__(self):
        return self.name
        
        
class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.name
    
class IngredientListing(models.Model):
    id = models.AutoField(primary_key=True)
    amount_numerator = models.PositiveSmallIntegerField(default=1)
    amount_denominator = models.PositiveSmallIntegerField(default=1)
    unit = models.ForeignKey( UnitOfMeasure, null=True, blank=True, default=None )
    ingredient = models.ForeignKey( Ingredient )
    optional = models.BooleanField( default=False )

    def __unicode__(self):
        number = "ERROR"
        if self.amount_denominator == 1:
            number = self.amount_numerator
        else:
            number = "{0}/{1}".format( self.amount_numerator, self.amount_denominator )
            
        unit = ""
        if self.unit:
            unit = "{0} ".format(self.unit)
            
        optional = ""
        if self.optional:
            optional = " (Optional)"
            
        return u"{0} {1}{2}{3}".format( number, unit, self.ingredient, optional )
    
class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    
    title = models.CharField(max_length=128)
    img = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)
    ingredient_list = models.ManyToManyField(IngredientListing)
    instructions = models.TextField(default="")
    
    attribution = models.CharField(max_length=64, null=True, blank=True)
    attribution_link = models.CharField(max_length=512, null=True, blank=True)
    
    created_by = models.ForeignKey(HMUser)
    created_date = models.DateTimeField(default=now)
    
    def image_thumbnail(self):
        return u"<img src=\"{0}\" height=\"64px\"></img>".format(self.img)
    image_thumbnail.short_description = 'Thumb'
    image_thumbnail.allow_tags = True
    
    
    def __unicode__(self):
        return self.title