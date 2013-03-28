from django.conf import settings
from django.http import HttpResponse

import json

from core.email import message_from_template
from store.models import Offer, Transaction
from giftcards.models import Giftcard

def fulfill_transaction(transaction):
    if transaction.offer.fulfillment == Offer.EGIFTCARD_EMAIL:
        fulfill_egiftcard(transaction)
        
    # do nothing for Offer.MANUAL
        
        
def fulfill_egiftcard(transaction, send_failure_email=True):    
    try:
        Giftcard.objects.get(transaction=transaction)
        return;
    except Giftcard.DoesNotExist:
        pass
        
    giftcard_inventory = Giftcard.objects.filter(transaction=None)
    
    if len(giftcard_inventory) == 0:
        
        if send_failure_email:
            email = message_from_template(
                "email/giftcard_inventory_empty.html",
                "the_server@healthfully.me",
                "noreply@healthfully.me",
                ["mortoc@healthfully.me"],
                [],
                {
                    "user" : transaction.user,
                    "transaction" : transaction,
                    "hostname" : settings.HOSTNAME
                }
            )
            email.send()
        return False
        
    else:
        purchased_card = giftcard_inventory[0]
        purchased_card.transaction = transaction
        purchased_card.save()
        
        transaction.notes = "Electronic Gift Card #{0}".format(purchased_card.card_id)
        transaction.shipping_tracking_data = "Emailed to {0}".format(purchased_card.fulfillment_url)
        transaction.save()
        
        email = message_from_template(
            "email/egiftcard_purchase_email.html",
            "orders@healthfully.me",
            "help@healthfully.me",
            [transaction.user.email],
            ["orders@healthfully.me"],
            {
                "user" : transaction.user,
                "transaction" : transaction,
                "giftcard" : purchased_card
            }
        )
        email.send()
        
        return True
        
def fulfill_egiftcard_direct(request, transaction_id):
    transaction = Transaction.objects.get(id_slug = transaction_id)
    
    if fulfill_egiftcard(transaction, False):
        return HttpResponse(
            json.dumps({"status" : "success"}), 
            mimetype="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({
                "status" : "fail",
                "message" : "Still no available inventory"
            }), 
            mimetype="application/json"
        )
        