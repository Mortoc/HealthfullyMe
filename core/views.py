from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.conf import settings
from django.http import HttpResponseRedirect


import hashlib

from core.email import message_from_template
from core.encode import base62_encode
from core.models import HMUser
from core.forms import SetPasswordForm

def server_error(request):
    return render_to_response(
            "server-error.html", 
            {}, 
            context_instance=RequestContext(request)
    )
    
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
        
        reset_url = request.get_host() + "/reset-password/" + hashlib.sha1(user_email + settings.SECRET_KEY).hexdigest()
        
#        email = message_from_template(
#            "email/reset_password_email.html",
#            "hello@healthfully.me",
#            "hello@healthfully.me",
#            [user.email],
#            ["hello@healthfully.me"],
#            { "reset_url" : reset_url }
#        )
#        email.send()
    print reset_url
    
    return render_to_response (
            'reset-password.html',
            context,
            context_instance=RequestContext(request)
        )
    
def set_my_password(request, key):
    if request.method == 'POST':
        form = SetPasswordForm(request.POST)
        
        if form.is_valid():
            return HttpResponseRedirect('/')

    else:
        form = SetPasswordForm()
         
    return render_to_response (
            'set_my_password.html',
            { 'form' : form },
            context_instance=RequestContext(request)
        )
    