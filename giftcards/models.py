from django.db import models
from django.utils.timezone import now
from django.conf import settings
from django.db.models.signals import post_save

from store.models import Transaction
class Giftcard(models.Model):
    
    #ex. TRADERJOES = 'TJS'
    WHOLEFOODSMARKET = 'WFM'
    ORGANIZATION_CHOICES = (
    # ex. (TRADERJOES, "Trader Joe's"),
        (WHOLEFOODSMARKET, 'Whole Foods Market'),
    )
    
    organization = models.CharField( max_length=4, choices=ORGANIZATION_CHOICES)
    card_id = models.BigIntegerField(unique=True, db_index=True)
    remaining_value = models.DecimalField(decimal_places=2, max_digits=16)
    created_date = models.DateTimeField(default=now)
    transaction = models.ForeignKey(Transaction, null=True, blank=True)
    fulfillment_url = models.CharField( max_length=128, null=True, blank=True)
    
    def is_sold(self):
        return self.transaction is not None
    
    is_sold.boolean = True
    is_sold.short_description = 'Is Sold?'
    
    def generate_fulfillment_url(self):
        if self.is_sold():
            self.fulfillment_url = "http://" + settings.HOSTNAME + "/giftcards/redeem-wholefoods-giftcard/" + self.transaction.id_slug 
            self.save()
            
            

def model_saved(sender, **kwargs):
    instance = kwargs['instance']
    if instance.fulfillment_url == None and instance.transaction != None:
        instance.generate_fulfillment_url()

post_save.connect(model_saved, sender=Giftcard)