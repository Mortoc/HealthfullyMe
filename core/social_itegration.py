from django.shortcuts import render, render_to_response
from django.template import RequestContext

def pinterest_verify(request):
	return render_to_response (
            'pinterest-8ecbe.html',
            {},
            context_instance=RequestContext(request)
        )