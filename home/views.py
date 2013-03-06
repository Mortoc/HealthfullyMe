from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

import hashlib

from core.validators import validate_email
from core.encode import email_to_username
from home.models import EmailRequest, AuthCode
from home.forms import UserLoginForm, UserRegistrationForm, EmailRequestForm

def enum(**enums):
    return type('Enum', (), enums)


def login_user(request):
    if request.user.is_authenticated():
        HttpResponseRedirect('/store/')
        
    error = None
    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = authenticate(username=email_to_username(email), password=password)
            
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                error = "Invalid Username or Password"
    else:
        form = UserLoginForm()
        
    return render_to_response (
            'login.html', { 
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
    
def register_user(request):
    if request.user.is_authenticated():
        HttpResponseRedirect('/store/')
        
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            auth_code = form.cleaned_data['invite_code']
            email = form.cleaned_data['email']
            username = email_to_username(email)
            password = form.cleaned_data['password']
            
            # create the user here but only save it if the auth code is good
            user = User.objects.create_user(username=username, email=email, password=password)
            
            auth_code_result = use_auth_code(auth_code, user)
            if auth_code_result == AuthCodeResult.SUCCESS:
                user.save()
                
                login(request, authenticate(username=username, password=password))
                       
                email = EmailMessage(
                    'Thank You For Your Purchase! - Healthfully Me', 
                    "Hi!\n\n" + 
                    "Thanks for creating your Healthfully Me account!  We know staying healthy can be tough so we're working on some new services and tools to make it easier, but we'd love to hear from you.\n\n" +
                    "In the meantime, want to save some money making those healthy meals at home?  Just login to our site to get exclusive access to 20% discount for your groceries at Whole Foods.\n\n" +   
                    "We'll have much more than just healthy savings very soon so check back often, and let us know what we can do to help you meet your health goals.\n\n" +  
                    "Your Healthfully Me Support Team,\n\n"
                    "Emily, Jamie, Brittany, and Caitlin",
                    'hello@healthfully.me',
                    [request.user.email], 
                    [],
                    headers = {'Reply-To': 'hello@healthfully.me'}
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


def index(request):
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
