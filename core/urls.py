from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # TODO: stop serving static files through gunicorn on heroku
    #  Obviously this isn't going to scale nicely - we're gonna want to put our static files on S3
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    
    url(r'^$', 'home.views.index', name='index'),
    
    url(r'^login', 'home.views.login_user', name='login'),
    url(r'^logout', 'home.views.logout_user', name='logout'),
    url(r'^register', 'home.views.register_user', name='register'),
    url(r'^submit-email', 'home.views.submit_email_request', name='submit-request'),
    url(r'^email-success', 'home.views.email_submission_success', name='submission-success'),
    url(r'^email-failure', 'home.views.email_submission_failure', name='submission-failure'),
    
    url(r'^store$', 'store.views.main', name='store'),
    url(r'^store/vote$', 'store.views.vote_ajax', name='vote'),
    url(r'^store/record-charge$', 'store.views.record_charge_ajax', name='record-charge'),
    url(r'^store/purchase-complete$', 'store.views.purchase_complete', name='purchase-complete'),
    url(r'^store/purchase-error$', 'store.views.purchase_error', name='purchase-error'),
    url(r'^store/offer-not-available/(?P<offer_id>.+)$', 'store.views.offer_not_available', name='offer-not-available'),
    
    url(r'^server-error', 'core.views.server_error', name='server-error'),
    
    url(r'^reset-password/(?P<key>.*)$', 'core.views.set_my_password'),
    
    url(r'^admin/tools/add-new-card', 'giftcards.views.add_new_card_ajax'),
    
    url(r'^fufill_egiftcard/(?P<transaction_id>.*)$', 'store.fulfillment.fulfill_egiftcard_direct'),
    
    url(r'^giftcards/redeem-wholefoods-giftcard/(?P<transaction_id>.+)$', 'giftcards.views.redeem_card'),
    url(r'^giftcards/redeem-wholefoods-giftcard-mobile/(?P<transaction_id>.+)$', 'giftcards.views.redeem_card_mobile'),
    url(r'^giftcards/redeem-wholefoods-giftcard-print/(?P<transaction_id>.+)$', 'giftcards.views.redeem_card_print'),
    
    url(r'^admin/tools/add-giftcards', 'giftcards.views.add_giftcards'),
    url(r'^admin/tools/email-viewer/(?P<email_name>.*)$', 'core.email.view_email'),
    url(r'^admin/tools/users-for-newsletter$', 'core.admintools.users_for_newsletter'),
    url(r'^admin/tools/reset-password/(?P<user_email>.*)$', 'core.views.reset_user_password'),
    
    url(r'^admin/tools$', 'core.views.all_tools'),
    
    url(r'^admin/', include(admin.site.urls)),
    
	url(r'^pinterest-8ecbe.html', 'core.social_itegration.pinterest_verify'),
)
