from django.conf.urls.defaults import *

urlpatterns = patterns('community.views',
    (r'^$', 'list_greetings'),
    (r'community/sign', 'create_greeting')
)