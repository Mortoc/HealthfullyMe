from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, RequestContext, Context
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.conf import settings
from core.htmlutil import minify_html
from store.models import Transaction

import re

SEND_EMAILS_IN_DEV = True
RE_FIND_TITLE_IN_HTML = re.compile('<title>(.+)</title>')

class __DevEmailMessage(EmailMessage):
    def send(self):
        pass

def message_from_template(template_path, from_email, reply_to, send_to, bcc = [], context={}):
    template = get_template( template_path )
    
    message = template.render( Context(context) )
    message = minify_html(message)
    
    subject = __get_email_subject_from_message(message)
    
    if settings.LIVE or SEND_EMAILS_IN_DEV:
        email = EmailMessage(
          subject,
          message,
          from_email,
          send_to,
          bcc,
          headers = { 'Reply-To': reply_to }
        )
    else:
        email = __DevEmailMessage(
          subject,
          message,
          from_email,
          send_to,
          bcc,
          headers = { 'Reply-To': reply_to }
        )
           
    email.content_subtype = "html"
    return email


def __get_email_subject_from_message(html_message):
    match = RE_FIND_TITLE_IN_HTML.search(html_message)
    
    if match:
        return match.group(1)
    
    return "NO TITLE FOUND"


def view_email(request, email_name):
    
    if request.user.is_authenticated() and request.user.is_staff:
        template = get_template("email/" + email_name)
        context = __get_special_context(request, email_name)
        
        return HttpResponse( template.render(RequestContext(request, context)) )
    
    else:
        return HttpResponseRedirect("/admin")
    
    
def __get_special_context(request, email_name):
    # put any specific context to be loaded for testing emails here
    
    if email_name == "purchase_confirmation.html" or \
       email_name == "notify_user_no_inventory_email.html":
        context = { }
        context["user"] = request.user
    
        transaction = Transaction.objects.filter(user=request.user).order_by('-timestamp')[0]    
        context["offer"] = transaction.offer
        context["transaction"] = transaction
        context["shipping_address"] = transaction.card.address
        context["billing_address"] = transaction.card.address

        return context
    else:
        return {}
        
    