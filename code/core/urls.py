from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', '/static/favicon.ico'),
    
    url(r'^$', 'home.views.index', name='index'),
    url(r'^login', 'home.login.views.login_user', name='login'),
    url(r'^logout', 'home.login.views.logout_user', name='logout'),
    url(r'^register', 'home.login.views.register_user', name='register'),
    url(r'^store$', 'store.views.main', name='store'),
    url(r'^store/vote$', 'store.views.vote_ajax', name='vote'),
    url(r'^store/record-charge$', 'store.views.record_charge_ajax', name='record-charge'),
    url(r'^submit-email', 'home.views.submit_email_request', name='submit-request'),
    url(r'^email-success', 'home.views.email_submission_success', name='submission-success'),
    url(r'^email-failure', 'home.views.email_submission_failure', name='submission-failure'),

    url(r'^admin/', include(admin.site.urls)),
)
