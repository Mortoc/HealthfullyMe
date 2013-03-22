from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.timezone import now
from django.conf import settings
from django.utils.safestring import mark_safe

import hashlib
import math
from datetime import timedelta

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
    
    availability = models.ManyToManyField('OfferAvailability', null=True, blank=True)
    
    def offer_price(self):
        return "${0:.2f}".format(float(self.price) * 0.01)
    
    def __unicode__(self):
        return self.header_text + " | " + self.offer_price()
    
    def user_can_purchase(self, user):
        transactions = Transaction.objects.filter(user = user.pk).order_by("-timestamp")
        
        if transactions.count() > 0:
            for rule in self.availability.all():
                if not rule.can_add_transaction(transactions):
                    return False
        
        return True
    
    def next_available_time(self, user):
        if self.user_can_purchase(user):
            return now()
        
        transactions = Transaction.objects.filter(user = user.pk).order_by("-timestamp")
        
        #print "\n\nChecking User Purchase"
        #print "{0} has {1} transactions".format(user.email, transactions.count())
        
        if transactions.count() > 0:
            next_availability = now()
            
            for rule in self.availability.all():
                if not rule.can_add_transaction(transactions):
                    start_time = rule.get_start_time()
    
                    first_rule_affected_trans = None
                    for transaction in transactions:
                        if transaction.timestamp > start_time:
                            first_rule_affected_trans = transaction
                        else:
                            break
                        
                    this_availability = first_rule_affected_trans.timestamp + rule.time_span()
                    
                    if not next_availability or this_availability > next_availability:
                        next_availability = this_availability
            
            print "##################"
            print show_time_as(next_availability, "EST")
            print "##################"
            return next_availability
        
        return now()
        

class OfferAvailability(models.Model):
    id = models.AutoField(primary_key=True)
    
    # potential user type key to have different 
    # availabilities for different types of users
    
    purchases = models.IntegerField(default=1)
    time_value = models.IntegerField(default=1)
    
    MINUTE = 0
    HOUR = 1
    DAY = 2
    MONTH = 3
    TIME_PEROID = (
        (MINUTE, 'Minutes'),
        (HOUR, 'Hours'),
        (DAY, 'Days'),
        (MONTH, 'Months'),
    )
    
    time_peroid = models.SmallIntegerField(choices=TIME_PEROID)
    
    def __unicode__(self):
        if self.purchases == 0:
            return "unlimited"
        
        time_unit = {
            0 : "minute",
            1 : "hour",
            2 : "day",
            3 : "month",
        }
        
        if self.purchases > 1:
            purchases_plural = "s"
        else:
            purchases_plural = ""
        
        if self.time_value == 1:
            return "{0} purchase{1} per {2}".format(self.purchases, purchases_plural, time_unit[self.time_peroid])
               
        if self.time_value > 1:
            time_value_plural = "s"
        else:
            time_value_plural = ""
        
        return "{0} purchase{1} per {2} {3}{4}".format(self.purchases, purchases_plural, self.time_value, time_unit[self.time_peroid], time_value_plural)
    
    # given a set of transactions, can we add another without violating this availability rule?
    def can_add_transaction(self, transactions = []):
        start_time = self.get_start_time()
        
        transactions_in_time_peroid = 0
        for transaction in transactions:
            if transaction.timestamp > start_time:
                transactions_in_time_peroid += 1
            else:
                break
        
        return transactions_in_time_peroid < self.purchases
            
    
    def time_span(self):
        if self.time_peroid == self.MINUTE:
            return timedelta(minutes=self.time_value)
        elif self.time_peroid == self.HOUR:
            return timedelta(hours=self.time_value)
        elif self.time_peroid == self.DAY:
            return timedelta(days=self.time_value)
        elif self.time_peroid == self.MONTH:
            return timedelta(days=self.time_value * 30)
        else:
            return timedelta()
    
    def get_start_time(self):
        return now() - self.time_span()

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
