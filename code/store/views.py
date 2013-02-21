from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import simplejson as json
import random
import sys
import stripe
from core import settings

from core import settings
from store.models import ComingSoonIdea, Offer, Transaction


def main(request):
    
    if request.user.is_anonymous():
        return HttpResponseRedirect("/")
    else:
        three_random_ideas = list(ComingSoonIdea.objects.order_by('?'))
        
        # This would be a really bad idea if we ever got a huge number of ComingSoonIdeas
        # but since it isn't a huge set, it's common to get non-unique entires
        
        while len(three_random_ideas) > 3:
            del three_random_ideas[ random.randint(0, len(three_random_ideas) - 1) ]
        
        return render(request, "store_main.html", 
        {
            "offer_list" : Offer.objects.filter(enabled = True),
            "stripe_public_key" : settings.STRIPE_PUBLIC_KEY,
            "idea1" : three_random_ideas[0],
            "idea2" : three_random_ideas[1],
            "idea3" : three_random_ideas[2],
        })
        
def record_charge_ajax(request):
    print "Recording Charge"
    
    stripe.api_key = settings.STRIPE_SECRET_KEY
    
    post_offer = Offer.objects.get(id = request.POST['offer_id'])
    post_stripe_token = request.POST['stripe_token']
    
    transaction = Transaction(user = request.user, offer = post_offer, stripe_token = post_stripe_token)
    
    print transaction
    
    try:
        stripe.Charge.create(
            amount = post_offer.price,
            currency = "usd",
            card = post_stripe_token,
            description = request.user.username
        )
    except stripe.AuthenticationError:
        print sys.exc_info()
        return HttpResponse( json.dumps("failure"), mimetype="application/json" )
    
    transaction.save()
    
    return HttpResponse( json.dumps("success"), mimetype="application/json" )

        
def vote_ajax(request):
    option1 = int(request.GET.get('option1', '-1'))
    idea1 = ComingSoonIdea.objects.get(id = option1)
    idea1.times_shown += 1
    print "1" + idea1.text
    idea1.save()
    
    option2 = int(request.GET.get('option2', '-1'))
    idea2 = ComingSoonIdea.objects.get(id = option2)
    idea2.times_shown += 1
    print "2" + idea2.text
    idea2.save()
    
    option3 = int(request.GET.get('option3', '-1'))
    idea3 = ComingSoonIdea.objects.get(id = option3)
    idea3.times_shown += 1
    print "3" + idea3.text
    idea3.save()
    
    selection = int(request.GET.get('selection', '-1'))
    
    selectionObj = None
    
    if selection == 1:
        selectionObj = ComingSoonIdea.objects.get(id = option1)
    elif selection == 2:
        selectionObj = ComingSoonIdea.objects.get(id = option2)
    elif selection == 3:
        selectionObj = ComingSoonIdea.objects.get(id = option3)
    else:
        return HttpResponse( json.dumps("failure"), mimetype="application/json" )
    
    selectionObj.times_selected += 1
    selectionObj.save()
    
    return HttpResponse( json.dumps("success"), mimetype="application/json" )