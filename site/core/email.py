from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, RequestContext, Context
from django.template.loader import get_template
from django.core.mail import EmailMessage
from core.htmlutil import minify_html

import re

RE_FIND_TITLE_IN_HTML = re.compile('<title>(.+)</title>')

def message_from_template(template_path, send_to, from_email, context={}):
    template = get_template( template_path )
    
    message = template.render( Context(context) )
    message = minify_html(message)
    
    subject = __get_email_subject_from_message(message)
    
    email = EmailMessage(
      subject,
      message,
      from_email,
      [send_to],
      [],
      headers={}
    )
    
    email.content_subtype = "html"
    
    print "Created Email:"
    print email
    print "To: " + send_to
    print "Subject: " + subject
    print "Message:\n" + message

    return email


def __get_email_subject_from_message(html_message):
    match = RE_FIND_TITLE_IN_HTML.search(html_message)
    
    if match:
        return match.group(1)
    
    return "NO TITLE FOUND"


def view(request, template_name):
    
    if request.user.is_authenticated() and request.user.is_staff:
      
        template = get_template("email/" + template_name)
        return HttpResponse( template.render(RequestContext(request)) )
    
    else:
        return HttpResponseRedirect("/")
    
    
