from django.conf.urls.defaults import *
from django.contrib.auth.forms import AuthenticationForm

from django.views.generic import RedirectView

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    url( '^$', RedirectView.as_view(url='http://signup.healthfully.me') ),
    
    (r'^$', include('community.urls')),
    
    (r'^giftcertificate', 'direct_to_template', {'template': 'giftcertificates/Mobile.html'}),
    
    (r'^accounts/create_user/$', 'community.views.create_new_user'),

    (r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'authentication_form': AuthenticationForm,
        'template_name': 'community/login.html',}),
        
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/',}),
)
