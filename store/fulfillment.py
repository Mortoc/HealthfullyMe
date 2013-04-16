from django.conf import settings
from django.http import HttpResponse

import json

from core.email import message_from_template
from store.models import Offer, Transaction
from giftcards.models import Giftcard

def fulfill_transaction(transaction):
    if transaction.offer.fulfillment == Offer.MANUAL:
        return fulfill_manual(transaction)
    elif transaction.offer.fulfillment == Offer.EGIFTCARD_EMAIL:
        return fulfill_egiftcard(transaction)
        
def fulfill_manual(transaction):        
    email = message_from_template(
        "email/purchase_confirmation.html",
        "orders@healthfully.me",
        "help@healthfully.me",
        [transaction.user.email],
        ["orders@healthfully.me"],
        {
            "user" : transaction.user,
            "offer" : transaction.offer,
            "transaction" : transaction,
            "shipping_address" : transaction.card.address.html(),
            "billing_address" : transaction.card.address.html()
        }
    )
    email.send()
    
    return True, {
        "offer" : transaction.offer,
        "transaction" : transaction,
        "shipping_address" : transaction.card.address.html(),
        "billing_address" : transaction.card.address.html(),
        "completed_order_copy" : transaction.offer.completed_order_copy
    }

def fulfill_egiftcard(transaction, send_failure_email=True):    
    try:
        Giftcard.objects.get(transaction=transaction) 
    except Giftcard.DoesNotExist:        
        giftcard_inventory = Giftcard.objects.filter(transaction=None)
    
        if len(giftcard_inventory) == 0:
            if send_failure_email:
                staff_email = message_from_template(
                    "email/giftcard_inventory_empty.html",
                    "the_server@healthfully.me",
                    "noreply@healthfully.me",
                    ["orders@healthfully.me"],
                    [],
                    {
                        "user" : transaction.user,
                        "transaction" : transaction,
                        "hostname" : settings.HOSTNAME,
                        "offer_name" : str(transaction.offer.buy_window_title)
                    }
                )
                user_email = message_from_template(
                    "email/notify_user_no_inventory_email.html",
                    "orders@healthfully.me",
                    "noreply@healthfully.me",
                    [transaction.user.email],
                    ["orders@healthfully.me"],
                    {
                        "user" : transaction.user,
                        "transaction" : transaction,
                        "offer_name" : str(transaction.offer.buy_window_title)
                    }
                )
                
                user_email.send()
                staff_email.send()
            return False, {}
        
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
                    "offer" : transaction.offer,
                    "giftcard" : purchased_card
                }
            )
            email.send()

    return True, {
        "offer" : transaction.offer,
        "transaction" : transaction,
        "shipping_address" : "Delivered via email",
        "billing_address" : transaction.card.address.html(),
        "completed_order_copy" : transaction.offer.completed_order_copy
    }
        
        
def fulfill_egiftcard_direct(request, transaction_id):
    transaction = Transaction.objects.get(id_slug = transaction_id)
    
    success, context = fulfill_egiftcard(transaction, False)
    
    if success:
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
        