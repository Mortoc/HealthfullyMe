from django.contrib import admin
from store.models import ComingSoonIdea, Offer, Transaction, Card

class ComingSoonIdeaAdmin(admin.ModelAdmin):
    list_display = ('text', 'selection_percentage', 'active')
    readonly_fields = ('times_shown', 'times_selected')
    
class OfferAdmin(admin.ModelAdmin):
    list_display = ('header_text', 'buy_window_description', 'offer_price', 'enabled')
    
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id_slug', 'user_email', 'card_info', 'offer', 'timestamp_in_est')
    
class CardAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'name', 'type', 'last4')
    readonly_fields = ('user', 'fingerprint', 'last4', 'type')
    
admin.site.register(ComingSoonIdea, ComingSoonIdeaAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Card, CardAdmin)