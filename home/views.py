from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.mail import EmailMessage

import hashlib

from core.ssl_utils import secure_required
from core.models import HMUser
from core.validators import validate_email
from core.email import message_from_template
from home.models import EmailRequest, AuthCode
from home.forms import UserLoginForm, UserRegistrationForm, EmailRequestForm



def enum(**enums):
    return type('Enum', (), enums)

@secure_required
def login_user(request):
    if request.user.is_authenticated():
        HttpResponseRedirect('/store/')
        
    error = None
    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = authenticate(email=email, password=password)
            
            if user is not None:
                
                if settings.DOWN_FOR_MAINTENANCE and not user.is_staff:
                    error = "The site is currently down for maintenance. Please try again later"
                else:
                    login(request, user)
                    return HttpResponseRedirect('/')
            else:
                error = "Invalid Username or Password"
    else:
        form = UserLoginForm()
        
    return render_to_response (
            'login.html', 
            { 
                'form': form,
                'error' : error 
            },
            context_instance=RequestContext(request)
        )
    
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
    
AuthCodeResult = enum(INVALID=0, PREVIOUSLY_USED=1, SUCCESS=2)
def use_auth_code(auth_code, user):
    try:
        auth = AuthCode.objects.get(code=auth_code)
        if auth.uses_left <= 0:
            return AuthCodeResult.PREVIOUSLY_USED
        
        auth.uses_left -= 1
        auth.registered_users.add(user)
        auth.save()
        return AuthCodeResult.SUCCESS
        
    except AuthCode.DoesNotExist:
        return AuthCodeResult.INVALID
    
@secure_required
def register_user(request):
    if request.user.is_authenticated():
        HttpResponseRedirect('/store/')
        
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            auth_code = form.cleaned_data['invite_code']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # create the user here but only save it if the auth code is good
            user = HMUser.objects.create_user(email=email, password=password)
            
            if settings.DOWN_FOR_MAINTENANCE and not user.is_staff:
                form._errors['invite_code'] = form.error_class(["The site is currently down for maintenance. Please try again later"])
                user.delete()
            else:
                auth_code_result = use_auth_code(auth_code, user)
                if auth_code_result == AuthCodeResult.SUCCESS:
                    user.receives_newsletter = form.cleaned_data['newsletter']
                    user.save()
                
                    user = authenticate(email=email, password=password)
                    login(request, user)
                
                    email = message_from_template(
                        "email/welcome_new_registration.html",
                        "hello@healthfully.me",
                        "hello@healthfully.me",
                        [user.email],
                        ["hello@healthfully.me"]
                    )
                    email.send()
                
                    return HttpResponseRedirect('/')
        
                elif auth_code_result == AuthCodeResult.PREVIOUSLY_USED:
                    user.delete()
                    form._errors['invite_code'] = form.error_class(["No uses left"])
            
                else:
                    user.delete()
                    form._errors['invite_code'] = form.error_class(["Invalid Code"])
            
    else:
        form = UserRegistrationForm()
             
    return render_to_response (
            'register.html',
            { 'form': form },
            context_instance=RequestContext(request)
        )

@secure_required
def index(request):
    if settings.DOWN_FOR_MAINTENANCE and not request.user.is_staff:
        return render(request, "down_for_maintenance.html", {});
        
    return render(request, "index.html", {
       'form' : EmailRequestForm()
    });
    
    
def submit_email_request(request):
    
    if request.method == 'POST':  # If the form has been submitted...
        form = EmailRequestForm(request.POST)  # A form bound to the POST data
        
        if form.is_valid():
            form_email = form.cleaned_data['email'].lower()
             
            # additional data verification
            if not validate_email(form_email):
                return HttpResponseRedirect('/email-failure')
            
            try:
                EmailRequest.objects.get(email=form_email)
            except EmailRequest.DoesNotExist:
                EmailRequest(email=form_email).save()

            return HttpResponseRedirect('/email-success')
        else:
            return HttpResponseRedirect('/email-failure')

    else:
        return index(request)


def email_submission_success(request):
    return render(request, "email_submission_success.html")


def email_submission_failure(request):
    return render(request, "email_submission_failure.html")
