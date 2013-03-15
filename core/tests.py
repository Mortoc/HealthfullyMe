from django.utils import unittest
from django.test.client import RequestFactory
from django.test import TestCase
from django.http import HttpResponseRedirect

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
            email="TEST@USER.COM",
            password="OMG_TESTS!"
        )
        
        
    def test_logins_are_recorded(self):
        request = self.factory.get('/login')
        request.session = MockSession()
        
        initial_logins = self.test_user.logins.count()
        self.test_user.login(request)
        
        self.assertEqual(initial_logins + 1, self.test_user.logins.count())