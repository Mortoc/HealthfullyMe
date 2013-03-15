from django.utils import unittest
from django.test.client import RequestFactory
from django.test import TestCase
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import AnonymousUser

from home.views import login_user
from core.models import *

class MockSession(dict):
    def __init__(self):
        self._dict = {}

    def add(self, id, val):
        self._dict[id] = val
        
    def cycle_key(self):
        pass
    
    def set_test_cookie(self):
        pass
    
class HMUserVerification(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        
        self.test_user = HMUser.objects.create_user (
            email="TEST@USER.COM".lower(),
            password="OMG_TESTS!"
        )
        
        self.test_user.save()
        
        
    def test_logins_are_recorded(self):
        request = self.factory.get('/login')
        request.user = AnonymousUser()
        request.session = MockSession()
        
        initial_logins = self.test_user.logins.count()

        request = self.factory.get('/login')
        request.user = AnonymousUser()
        request.session = MockSession()
        
        request.method = "POST"
        request.POST = {
            'email' : 'test@user.com',
            'password' : 'OMG_TESTS!',
        }
        
        response = login_user(request)
        
        user = HMUser.objects.get(email = 'test@user.com')
        self.assertEqual(initial_logins + 1, user.logins.count())