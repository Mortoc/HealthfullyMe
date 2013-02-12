from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'home.views.index', name='index'),
    url(r'^submit-email', 'home.views.submit_email_request', name='submit-request'),
    url(r'^email-success', 'home.views.email_submission_success', name='submission-success'),
    url(r'^email-failure', 'home.views.email_submission_failure', name='submission-failure'),

    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/images/favicon.ico'}),
    
    url(r'^admin/', include(admin.site.urls)),
)
