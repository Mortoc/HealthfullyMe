from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.timezone import now
from django.conf import settings
from django.utils.safestring import mark_safe

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
            return "{0:.0f} %".format(float(100 * self.times_selected) / float(self.times_shown))
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
        return "${0:.2f}".format(float(self.price) * 0.01)
    
    def __unicode__(self):
        return self.header_text + " | " + self.offer_price()

class Card(models.Model):    
    @staticmethod
    def __clean_input(input):
        if input is None:
            return ""
        return input
        
    @staticmethod
    def from_stripe_charge(charge, user):
        try:
            card = Card.objects.get(fingerprint=charge.card.fingerprint)
        except Card.DoesNotExist:
            address = Address(
                name=Card.__clean_input(charge.card.name),
                line1=Card.__clean_input(charge.card.address_line1),
                line2=Card.__clean_input(charge.card.address_line2),
                city=Card.__clean_input(charge.card.address_city),
                state=Card.__clean_input(charge.card.address_state),
                zip=Card.__clean_input(charge.card.address_zip),
                country=Card.__clean_input(charge.card.address_country),
            )
            address.save()
            
            card = Card(
                user=user,
                name=Card.__clean_input(charge.card.name),
                fingerprint=Card.__clean_input(charge.card.fingerprint),
                last4=Card.__clean_input(charge.card.last4),
                address=address,
                type=Card.__clean_input(charge.card.type),
                expire_month=int(charge.card.exp_month),
                expire_year=int(charge.card.exp_year)
            )
            card.save()
            
        return card
        
    
    def address_for_admin(self):
        return mark_safe("<p>{0}<br /><a href='/admin/core/address/{1}'>edit</a></p>".format(self.address.html(), self.address.pk))
    
    address_for_admin.allow_tags = True
    address_for_admin.short_description = "Address"
        
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=256)  # name used on credit card
    fingerprint = models.CharField(max_length=128)
    last4 = models.CharField(max_length=4)
    
    address = models.ForeignKey(Address, null=True, default=None)
    
    type = models.CharField(max_length=32)
    expire_month = models.IntegerField(null=True)
    expire_year = models.IntegerField(null=True)    
    
    def user_email(self):
        return self.user.email
    
    def __unicode__(self):
        return self.name + " | " + self.type + " | " + self.last4
    

ID_SLUG_LENGTH = 16
PRIVATE_TRANSACTION_KEY = 349659
class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    id_slug = models.CharField(max_length=ID_SLUG_LENGTH, null=True, blank=True)
    stripe_id = models.CharField(max_length=64, null=True, blank=True)
    shipping_tracking_data = models.CharField(max_length=255, null=True, blank=True)
    shipped = models.BooleanField(default=False)
    offer = models.ForeignKey(Offer)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    card = models.ForeignKey(Card, null=True)
    timestamp = models.DateTimeField(default=now)
    notes = models.TextField(default="", null=True, blank=True)
    
    def timestamp_in_est(self):
        return show_time_as(self.timestamp, 'America/New_York')
    
    def shipping_address(self):
        return self.card.address.__unicode__()
    
    def card_info(self):
        return "{0}  |  ...{1}".format(self.card.type, self.card.last4)
    
    def generate_id_slug(self):
        
        # if this offer id is a 6 digit number, we won't have room for it in the id_slug field
        if self.offer.id > 99999:
            self.id_slug = "error 56";
        
        self.id_slug = str(self.offer.id) + "x" + str(self.id) + "x" + hashlib.sha1(str(PRIVATE_TRANSACTION_KEY + int(self.id))).hexdigest()[:ID_SLUG_LENGTH - 7]
        self.save()
        
    def set_shipping(self):
        if not self.shipping_tracking_data:
            return 
        
        if len(self.shipping_tracking_data) > 2 and not self.shipped:
            self.shipped = True
            self.save()
        elif len(self.shipping_tracking_data) <= 2 and self.shipped:
            self.shipped = False
            self.save()
        
        
def model_saved(sender, **kwargs):
    instance = kwargs['instance']
    if kwargs['created']:
        instance.generate_id_slug()

    instance.set_shipping()

post_save.connect(model_saved, sender=Transaction)
