from django.contrib import admin
from store.models import ComingSoonIdea, Offer, Transaction

class ComingSoonIdeaAdmin(admin.ModelAdmin):
    list_display = ('text', 'selection_percentage')
    readonly_fields = ('times_shown', 'times_selected')
    
class OfferAdmin(admin.ModelAdmin):
    list_display = ('header_text', 'buy_window_description', 'offer_price', 'enabled')
    
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('stripe_token', 'user', 'offer', 'timestamp')
    
admin.site.register(ComingSoonIdea, ComingSoonIdeaAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Transaction, TransactionAdmin)
