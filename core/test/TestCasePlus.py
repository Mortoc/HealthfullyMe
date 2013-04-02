from django.test import TestCase
from django.test.client import Client, RequestFactory

class TestCasePlus(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        
        
    def do_login(self, email, password):
        return self.secure_post('/login', {
            'email' : email,
            'password' : password,
        })
        
        
    def get_secure_request(self, url):
        kwargs = {}
        kwargs["wsgi.url_scheme"] = "https"
        kwargs["HTTP_X_REQUESTED_WITH"] = 'XMLHttpRequest'
        return self.factory.get(url, **kwargs)
        
    def secure_post(self, url, data = {}, follow=True):
        client = Client()
        kwargs = {}
        kwargs["wsgi.url_scheme"] = "https"
        kwargs["HTTP_X_REQUESTED_WITH"] = 'XMLHttpRequest'
        
        return client.post(url, data, follow=follow, **kwargs)
        
    def secure_get(self, url, follow=True):
        client = Client()
        kwargs = {}
        kwargs["wsgi.url_scheme"] = "https"
        kwargs["HTTP_X_REQUESTED_WITH"] = 'XMLHttpRequest'
        
        return client.get(url, follow=follow, **kwargs)