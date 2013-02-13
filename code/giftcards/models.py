from django.db import models
from django.utils import timezone

class Giftcard(models.Model):
	
	#ex. TRADERJOES = 'TJS'
	WHOLEFOODSMARKET = 'WFM'
	ORGANIZATION_CHOICES = (
	# ex. (TRADERJOES, "Trader Joe's"),
		(WHOLEFOODSMARKET, 'Whole Foods Market'),
	)
	
	organization = models.CharField( max_length=4, choices=ORGANIZATION_CHOICES)
	card_id = models.BigIntegerField()
	remaining_value = models.DecimalField(decimal_places=2, max_digits=16)
	assigned_to = models.EmailField(null=True)
	created_date = models.DateTimeField(default=timezone.now())
	sold_date = models.DateTimeField(null=True)
	
	
	def is_sold(self):
		return self.assigned_to is not None

	is_sold.admin_order_field = 'sold_date'
	is_sold.boolean = True
	is_sold.short_description = 'Is Sold?'