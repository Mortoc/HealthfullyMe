from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext, loader
from home.models import EmailRequest


def index(request):

    if request.method == 'POST': # If the form has been submitted...
        form = EmailRequest(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = EmailRequest() # An unbound form

    return render(request, "index.html", {
       'form' : form                                   
    });