from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import simplejson as json
import random
import sys
import stripe

from core import settings
from store.models import ComingSoonIdea, Offer, Transaction


def main(request):
    if request.user.is_anonymous():
        return HttpResponseRedirect("/")
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
        
def purchase_complete(request):
    recent_transaction = Transaction.objects.filter(user=request.user).order_by('timestamp')[0]
    recent_offer = recent_transaction.offer;
    
    return render(request, "purchase_complete.html",
    {
        "offer" : recent_offer,
        "transaction" : recent_transaction
    })
    
def purchase_error(request):
    return render(request, "purchase_error.html", {})
    

def run_stripe_charge(price, stripe_token, username):
    return stripe.Charge.create(
        amount=price,
        currency="usd",
        card=stripe_token,
        description=username
    )
        
def record_charge_ajax(request, run_charge=run_stripe_charge):
    try:
        stripe.api_key = settings.STRIPE_SECRET_KEY
        
        post_offer = Offer.objects.get(id=int(request.POST['offer_id']))
        post_stripe_token = request.POST['stripe_token']
        
        transaction = Transaction(
            user=request.user,
            offer=post_offer,
            stripe_token=post_stripe_token
        )
        
        charge = run_charge(
            post_offer.price,
            post_stripe_token,
            request.user.username 
        )
        
        transaction.save()
        
        return HttpResponse(json.dumps( {"status" : "success"} ), mimetype="application/json")
    except (stripe.StripeError, stripe.CardError) as e:
        response_data = {
            "status" : "card-declined",
            "message" : e.param,
            "code" : e.code
        }
        return HttpResponse(json.dumps(response_data), mimetype="application/json")
    except:
        response_data = {
            "status" : "server-error",
            "message" : "A Non-stripe error occured"
        }
        
        return HttpResponse(json.dumps(response_data), mimetype="application/json")

        
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
    
    selectionObj = None
    
    if selection == 1:
        selectionObj = ComingSoonIdea.objects.get(id=option1)
    elif selection == 2:
        selectionObj = ComingSoonIdea.objects.get(id=option2)
    elif selection == 3:
        selectionObj = ComingSoonIdea.objects.get(id=option3)
    else:
        return HttpResponse(json.dumps("failure"), mimetype="application/json")
    
    selectionObj.times_selected += 1
    selectionObj.save()
    
    return HttpResponse(json.dumps("success"), mimetype="application/json")
