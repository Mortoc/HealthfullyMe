from django.utils import unittest
from django.test.client import RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.test import TestCase
from django.http import HttpResponseRedirect

from home.views import *
from home.models import *
from core.models import *
from core.encode import *

class MockSession(dict):
    def __init__(self):
        self._dict = {}

    def add(self, id, val):
        self._dict[id] = val
        
    def cycle_key(self):
        pass

class RegistrationVerification(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        
        self.test_user = HMUser.objects.create_user (
            email="TEST@USER.COM",
            password="OMG_TESTS!"
        )
        
        self.auth_code = AuthCode()
        self.auth_code.save()
        
        
    def auth_code_generation(self):
        auth = AuthCode()
        auth.save()
        
        self.assertEqual(len(auth.code), home.models.CODE_LENGTH, "Saving the auth code should generate a code")
        
        
    def test_register_existing_username(self):
        existing_user_count = HMUser.objects.all().count()
        request = self.factory.get('/register')
        request.user = AnonymousUser()
        request.session = MockSession()
 
        request.method = "POST"
        request.POST = {
            'invite_code' : self.auth_code.code,
            'email' : 'test@user.com',
            'password' : 'test_password',
            'password_again' : 'test_password'
        }
        
        response = register_user(request)
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], "/")
        self.assertEqual(existing_user_count + 1, HMUser.objects.all().count())
        
        
    def test_register_long_username(self):
        existing_user_count = HMUser.objects.all().count()
        request = self.factory.get('/register')
        request.user = AnonymousUser()
        request.session = MockSession()
        
        email = "T1234567890123456789012345678901234567@reallylongwebsitedomain.com.om"
        
        request.method = "POST"
        request.POST = {
            'invite_code' : self.auth_code.code,
            'email' : email,
            'password' : 'test_password',
            'password_again' : 'test_password'
        }
        
        response = register_user(request)
        
        created_user = HMUser.objects.get(email=email.lower())
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], "/")
        self.assertEqual(existing_user_count + 1, HMUser.objects.all().count())
        
        
    def test_register_invalid_auth_declines(self):
        existing_user_count = HMUser.objects.all().count()
        
        request = self.factory.get('/register')
        request.user = AnonymousUser()
        request.session = MockSession()
 
        request.method = "POST"
        request.POST = {
            'auth_code' : 'nocode',
            'email' : 'test_register_invalid_auth_declines@test.com',
            'password' : 'test_password',
            'password_again' : 'test_password'
        }
        
        response = register_user(request)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(existing_user_count, HMUser.objects.all().count(), "Invalid auth code still created a user")
