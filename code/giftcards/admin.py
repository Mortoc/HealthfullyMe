from django.contrib import admin
from giftcards.models import Giftcard

class GiftcardAdmin(admin.ModelAdmin):
    list_display = ('organization', 'card_id', 'is_sold')
        
admin.site.register(Giftcard, GiftcardAdmin)