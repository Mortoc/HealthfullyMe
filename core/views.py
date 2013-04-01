from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils.timezone import now 

import sys, traceback
import hashlib

from core.ssl_utils import secure_required
from core.email import message_from_template
from core.encode import base62_encode
from core.models import HMUser, UserAccessCode
from core.forms import SetPasswordForm

def server_error(request):
    return render_to_response(
            "server-error.html", 
            {}, 
            context_instance=RequestContext(request)
    )
    
@secure_required
def reset_user_password(request, user_email):
    
    # only staff can reset a user's password with this page
    if not request.user.is_staff:
        HttpResponseRedirect('/')
        
    context = { 'user_email' : user_email }
    
    try:
        user = HMUser.objects.get(email = user_email)
    except HMUser.DoesNotExist:
        context['error'] = "There is not user with the email '" + user_email + "'"
    
    if request.POST:
        context['message'] = "An email has been sent to " + user_email + " with a link to reset their password"
        
        access = UserAccessCode.create(HMUser.objects.get(email = user_email))
        access.save()
        
        reset_url = "http://" + request.get_host() + "/reset-password/" + access.code 
        
        email = message_from_template(
            "email/reset_password_email.html",
            "help@healthfully.me",
            "help@healthfully.me",
            [user.email],
            ["help@healthfully.me"],
            { "reset_url" : reset_url }
        )
        email.send()
    
    return render_to_response (
            'reset-password.html',
            context,
            context_instance=RequestContext(request)
        )
    
@secure_required
def set_my_password(request, key):
    context = { 'code' : key }
    form = None
    
    try:
        code = UserAccessCode.objects.get(code = key)
        if code.valid_until < now():
            context['error'] = "Expired Code"
        elif request.method == 'POST':
            form = SetPasswordForm(request.POST)
            
            if form.is_valid():
                print form.cleaned_data["password"]
                user = HMUser.objects.get(email = code.user.email)
                user.set_password(form.cleaned_data["password"])
                user.save()
                code.delete()
                context['message'] = "Password has been reset"
        else:
            form = SetPasswordForm()
                    
    except:
        if not settings.TEST:
            print sys.exc_info()
            print sys.exc_value
            print traceback.format_exc()
        
        context['error'] = "Invalid Code"
    
    
    if form:    
        context['form'] = form
    
    return render_to_response (
            'set_my_password.html',
            context,
            context_instance=RequestContext(request)
        )
    