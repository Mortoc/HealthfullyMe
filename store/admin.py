from django.contrib import admin
from store.models import ComingSoonIdea, Offer, Transaction, Card
from core.models import Address


class ComingSoonIdeaAdmin(admin.ModelAdmin):
    list_display = ('text', 'selection_percentage', 'active')
    readonly_fields = ('times_shown', 'times_selected')
    
class OfferAdmin(admin.ModelAdmin):
    list_display = ('header_text', 'buy_window_description', 'offer_price', 'enabled')
    
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id_slug', 'user', 'card_info', 'offer', 'timestamp_in_est', 'shipped')
    readonly_fields = ('id_slug', 'shipped', )
    
class CardAdmin(admin.ModelAdmin):
    fields = ('user', 'fingerprint', 'last4', 'type', 'expire_month', 'expire_year', 'name', 'address', )
    list_display = ('user_email', 'name', 'type', 'last4',)
    
    
admin.site.register(ComingSoonIdea, ComingSoonIdeaAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Card, CardAdmin)
