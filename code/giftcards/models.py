from django.db import models
from django.utils import timezone
from django.contrib import admin

class Giftcard(models.Model):
	
	#ex. TRADERJOES = 'TJS'
	WHOLEFOODSMARKET = 'WFM'
	ORGANIZATION_CHOICES = (
	# ex. (TRADERJOES, "Trader Joe's"),
		(WHOLEFOODSMARKET, 'Whole Foods Market'),
	)
	
	organization = models.CharField( max_length=4, choices=ORGANIZATION_CHOICES)
	cardId = models.BigIntegerField()
	remainingValue = models.DecimalField(decimal_places=2, max_digits=16)
	assignedTo = models.EmailField(null=True)
	cardLoadedDate = models.DateTimeField(default=timezone.now())
	cardSoldDate = models.DateTimeField(null=True)
	
	def isSold(self):
		return self.assignedTo is not None
		
admin.site.register(Giftcard)