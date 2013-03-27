from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, Template

import json, sys, traceback

from core import settings
from giftcards.models import Giftcard
from store.models import Transaction

def add_giftcards(request):
    if not request.user.is_staff:
        return HttpResponseRedirect('/')
        
    return render(request, "add-giftcard.html", {})
    
    
def add_new_card_ajax(request):
    #try:
    remaining_value = 5000
    card_id = int(request.POST['card_id'])
    exists = True
    try:
        Giftcard.objects.get(card_id=card_id)
    except Giftcard.DoesNotExist:
        exists = False
    
    if not exists:
        Giftcard(
            organization=Giftcard.WHOLEFOODSMARKET, 
            card_id=card_id, 
            remaining_value=remaining_value
        ).save()
    
        return HttpResponse(
            json.dumps({"status" : "success"}), 
            mimetype="application/json"
        )
    else:
        
        return HttpResponse(
            json.dumps({
                "status" : "error",
                "message" : "Card ({0}) already exists".format(card_id)
            }), 
            mimetype="application/json"
        )
        
'''    except:
        response_data = {
            "status" : "server-error",
            "message" : "{0}\n{1}\n{2}".format( sys.exc_info(), sys.exc_value, traceback.format_exc() )
        }
        
        return HttpResponse(
            json.dumps(response_data), 
            mimetype="application/json"
        )'''
        