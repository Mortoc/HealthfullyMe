from django.http import HttpResponseRedirect
from django.shortcuts import render
from home.models import EmailRequest, EmailRequestForm
import string
import re


def validateEmail(email):
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return 1
    return 0

def index(request):
    return render(request, "index.html", {
       'form' : EmailRequestForm()                                   
    });
    
    
def submit_email_request(request):
    
    if request.method == 'POST': # If the form has been submitted...
        form = EmailRequestForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            form_email = string.lower(form['email'].data)
            
            # additional data verification
            if not validateEmail(form_email):
                return HttpResponseRedirect('/email-failure/')
            
            try:
                EmailRequest.objects.get(email = form_email)
            except EmailRequest.DoesNotExist:
                EmailRequest(email = form_email).save()

            return HttpResponseRedirect('/email-success/')
        else:
            return HttpResponseRedirect('/email-failure/')

    else:
        return index(request)


def email_submission_success(request):
    return render(request, "email_submission_success.html")


def email_submission_failure(request):
    return render(request, "email_submission_failure.html")