from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'home.views.index', name='index'),
    url(r'^submit_email_request', 'home.views.submit_email_request', name='submit_email_request'),
    url(r'^email_submition_success', 'home.views.email_submition_success', name='email_submition_success'),
    url(r'^email_submition_failure', 'home.views.email_submition_failure', name='email_submition_failure'),

    url(r'^admin/', include(admin.site.urls)),
)
