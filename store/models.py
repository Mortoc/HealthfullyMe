from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.timezone import now

import hashlib
import math

from core.encode import base62_encode
from core.timeutil import show_time_as
from core.models import Address

class ComingSoonIdea(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=160)
    times_shown = models.IntegerField(default=0)
    times_selected = models.IntegerField(default=0)
    active = models.BooleanField(default=False)
    
    def selection_percentage(self):
        if self.times_shown > 0:
            return "{0:.0f} %".format( float(100 * self.times_selected) / float(self.times_shown) )
        else:
            return "Not Yet Shown"


class Offer(models.Model):
    id = models.AutoField(primary_key=True)
    header_text = models.CharField(max_length=128)
    description_line_1 = models.CharField(max_length=96, default="", null=True, blank=True)
    description_line_2 = models.CharField(max_length=96, default="", null=True, blank=True)
    description_line_3 = models.CharField(max_length=96, default="", null=True, blank=True)
    description_line_4 = models.CharField(max_length=96, default="", null=True, blank=True)
    description_line_5 = models.CharField(max_length=96, default="", null=True, blank=True)
    image = models.CharField(max_length=128, default="/static/img/product/wholefoods.jpg")
    thumbnail_image = models.CharField(max_length=128, default="/static/img/product/wholefoods128.png")
    buy_window_title = models.CharField(max_length=64)
    buy_window_description = models.CharField(max_length=64, null=True)
    price = models.IntegerField(default=4000)
    enabled = models.BooleanField(default=False)
    
    def offer_price(self):
        return "${0:.2f}".format( float(self.price) * 0.01 )
    
    def __unicode__(self):
        return self.header_text + " | " + self.offer_price()

class Card(models.Model):
    @staticmethod
    def clean(charge_data):
        if charge_data is None:
            return ""
        
        return charge_data
    
    
    @staticmethod
    def from_stripe_charge(charge, user):
        try:
            card = Card.objects.get(fingerprint = charge.card.fingerprint)
        except Card.DoesNotExist:
            address = Address(
                name = Card.clean(charge.card.name),
                line1 = Card.clean(charge.card.address_line1),
                line2 = Card.clean(charge.card.address_line2),
                city = Card.clean(charge.card.address_city),
                state = Card.clean(charge.card.address_state),
                zip = Card.clean(charge.card.address_zip),
                country = Card.clean(charge.card.address_country),
            )
            address.save()
            
            card = Card(
                user = user,
                name = Card.clean(charge.card.name),
                fingerprint = Card.clean(charge.card.fingerprint),
                last4 = Card.clean(charge.card.last4),
                address = address,
                type = Card.clean(charge.card.type),
                expire_month = int(charge.card.exp_month),
                expire_year = int(charge.card.exp_year)
            )
            card.save()
            
        return card
        
        
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    name = models.CharField(max_length=256) #name used on credit card
    fingerprint = models.CharField(max_length=128)
    last4 = models.CharField(max_length=4)
    
    address = models.ForeignKey(Address, null=True, default=None)
    
    type = models.CharField(max_length=32)
    expire_month = models.IntegerField(null=True)
    expire_year = models.IntegerField(null=True)    
    
    def user_email(self):
        return self.user.email
    
    def __unicode__(self):
        return self.type + " | " + self.last4
    

ID_SLUG_LENGTH = 16
PRIVATE_TRANSACTION_KEY = 349659
class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    id_slug = models.CharField(max_length=ID_SLUG_LENGTH, default='')
    offer = models.ForeignKey( Offer )
    user = models.ForeignKey( User )
    card = models.ForeignKey( Card, null=True )
    timestamp = models.DateTimeField(default=now)
    
    def timestamp_in_est(self):
        return show_time_as(self.timestamp, 'America/New_York')
    
    def user_email(self):
        return self.user.email
    
    def card_info(self):
        return "{0}  |  ...{1}".format(self.card.type, self.card.last4)
    
    def generate_id_slug(self):
        
        # if this offer id is a 6 digit number, we won't have room for it in the id_slug field
        if self.offer.id > 99999:
            self.id_slug = "error 56";
        
        self.id_slug = str(self.offer.id) + "x" + str(self.id) + "x" + hashlib.sha1( str(PRIVATE_TRANSACTION_KEY + int(self.id)) ).hexdigest()[:ID_SLUG_LENGTH - 7]
        self.save()
        
        
def model_created(sender, **kwargs):
    instance = kwargs['instance']
    if kwargs['created']:
        instance.generate_id_slug()

post_save.connect(model_created, sender=Transaction)