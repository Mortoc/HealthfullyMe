from django.shortcuts import render, render_to_response
from django.template import RequestContext

def server_error(request):
    return render_to_response(
            "server-error.html", 
            {}, 
            context_instance=RequestContext(request)
    )