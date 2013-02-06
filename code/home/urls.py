from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'home.views.index', name='index'),
    url(r'^/submit_email_request/', 'home.views.submit_email_request', name='submit_email_request')
)
