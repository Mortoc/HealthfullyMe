from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, Template
from django.conf import settings

import json
import random
import sys
import stripe
import traceback

from core.ssl_utils import secure_required
from core.email import message_from_template
from store.models import ComingSoonIdea, Offer, Transaction, Card
from store.fulfillment import fulfill_transaction

@secure_required
def main(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login")
    else:
        three_random_ideas = list(ComingSoonIdea.objects.filter(active=True).order_by('?'))
        
        while len(three_random_ideas) > 3:
            del three_random_ideas[ random.randint(0, len(three_random_ideas) - 1) ]
        
        context = {
            "offer_list" : Offer.objects.filter(enabled=True),
            "stripe_public_key" : settings.STRIPE_PUBLIC_KEY
        }
        
        if len(three_random_ideas) > 0:
            context["idea1"] = three_random_ideas[0]
            
        if len(three_random_ideas) > 1:
            context["idea2"] = three_random_ideas[1]
            
        if len(three_random_ideas) > 2:
            context["idea3"] = three_random_ideas[2] 
        
        return render(request, "store_main.html", context)
        
@secure_required
def purchase_complete(request):
    recent_transaction = Transaction.objects.filter(user=request.user.pk).order_by('-timestamp')[0]
    recent_offer = recent_transaction.offer;
    
    success, context = fulfill_transaction( recent_transaction )
    
    if success:
        return render(request, "purchase_complete.html", context)
    else:
        return render(request, "inventory_exhausted.html", context)
        
@secure_required
def purchase_error(request):
    return render(request, "purchase_error.html", {})
    

def run_stripe_charge(price, stripe_token, username):
    return stripe.Charge.create(
        amount=price,
        currency="usd",
        card=stripe_token,
        description=username
    )

@secure_required        
def record_charge_ajax(request, run_charge=run_stripe_charge):
    try:
        stripe.api_key = settings.STRIPE_SECRET_KEY
        
        post_offer = Offer.objects.get(id=int(request.POST['offer_id']))
        post_stripe_token = request.POST['stripe_token']
        
        if post_offer.user_can_purchase(request.user):
            
            charge = run_charge(
                post_offer.price,
                post_stripe_token,
                request.user.email 
            )
            
            card = Card.from_stripe_charge(charge, request.user)
            
            transaction = Transaction(
                user=request.user,
                offer=post_offer,
                card=card,
                stripe_id=charge.id
            )
            transaction.save()
            
            return HttpResponse(json.dumps({"status" : "success"}), mimetype="application/json")
        
        else:
            response_data = {
                "status" : "not-available",
                "offer_id" : post_offer.id
            }
            
            return HttpResponse(json.dumps(response_data), mimetype="application/json")
            
    except (stripe.StripeError, stripe.CardError) as e:
        response_data = {
            "status" : "card-declined",
            "message" : e.param,
            "code" : e.code
        }
        
        if not settings.TEST:
            print "Card Declined"
            print sys.exc_info()
            print sys.exc_value
            print traceback.format_exc()
        
        return HttpResponse(json.dumps(response_data), mimetype="application/json")
    except:
        response_data = {
            "status" : "server-error",
            "message" : "A Non-stripe error occured"
        }
        
        if not settings.TEST:
            print "Server Error"
            print sys.exc_info()
            print sys.exc_value
            print traceback.format_exc()
        
        return HttpResponse(json.dumps(response_data), mimetype="application/json")
        
@secure_required
def offer_not_available(request, offer_id):
    return render(request, "offer_not_available.html",
    {
        "available_date" : Offer.objects.get(id=offer_id).next_available_time(request.user)
    })

        

def vote_ajax(request):
    option1 = int(request.GET['option1'])
    idea1 = ComingSoonIdea.objects.get(id=option1)
    idea1.times_shown += 1
    idea1.save()
    
    option2 = int(request.GET['option2'])
    idea2 = ComingSoonIdea.objects.get(id=option2)
    idea2.times_shown += 1
    idea2.save()
    
    option3 = int(request.GET['option3'])
    idea3 = ComingSoonIdea.objects.get(id=option3)
    idea3.times_shown += 1
    idea3.save()
    
    selection = int(request.GET['selection'])
    
    selection_obj = None
    
    if selection == 1:
        selection_obj = ComingSoonIdea.objects.get(id=option1)
    elif selection == 2:
        selection_obj = ComingSoonIdea.objects.get(id=option2)
    elif selection == 3:
        selection_obj = ComingSoonIdea.objects.get(id=option3)
    else:
        return HttpResponse(json.dumps("failure"), mimetype="application/json")
    
    selection_obj.times_selected += 1
    selection_obj.save()
    
    return HttpResponse(json.dumps("success"), mimetype="application/json")
