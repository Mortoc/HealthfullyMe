from django.http import HttpResponseRedirect
from django.shortcuts import render
from home.models import EmailRequest, EmailRequestForm


def index(request):
    return render(request, "index.html", {
       'form' : EmailRequestForm()                                   
    });
    
    
def submit_email_request(request):
    
    if request.method == 'POST': # If the form has been submitted...
        form = EmailRequestForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            form_email = form['email'].data
            
            try: 
                EmailRequest.objects.get(email = form_email)
            except EmailRequest.DoesNotExist:
                print( "Creating new email request: " + form_email)
                EmailRequest(email = form_email).save()

            return HttpResponseRedirect('/email_submition_success/')
        else:
            return HttpResponseRedirect('/email_submition_failure/')

    else:
        return index(request)


def email_submition_success(request):
    return render(request, "email_submition_success.html")


def email_submition_failure(request):
    return render(request, "email_submition_failure.html")