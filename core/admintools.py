from django.http import HttpResponseRedirect, HttpResponse

from UserString import MutableString
from core.models import HMUser


def users_for_newsletter(request):
    if request.user.is_authenticated() and request.user.is_staff:
        
        list = MutableString()
        
        for user in HMUser.objects.filter(receives_newsletter=True):
            list += user.email + ",\n"
        
        return HttpResponse(list, mimetype="text/plain")
    
    else:
        return HttpResponseRedirect("/admin")