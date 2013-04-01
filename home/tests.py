from django.utils import unittest
from django.test.client import Client, RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.test import TestCase
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

from home.views import *
from home.models import *
from core.models import *
from core.encode import *

from core.test.TestCasePlus import TestCasePlus

class MockSession(dict):
    def __init__(self):
        self._dict = {}

    def add(self, id, val):
        self._dict[id] = val
        
    def cycle_key(self):
        pass
    
class LoginVerification(TestCasePlus):
    def setUp(self):
        super(LoginVerification, self).setUp()
        
        self.test_user = HMUser.objects.create_user (
            email="TEST@USER.COM".lower(),
            password="OMG_TESTS!"
        )
        self.test_user.save()
        
        self.auth_code = AuthCode()
        self.auth_code.save()
        
        
    def test_login(self):
        client = Client()
        request = client.post('/login', { 'email' : 'test@user.com', 'password' : 'OMG_TESTS!' })
        
        user = HMUser.objects.get(email = "test@user.com")
        self.assertTrue(user.is_authenticated)


class RegistrationVerification(TestCasePlus):
    def setUp(self):        
        self.test_user = HMUser.objects.create_user(
            email="TEST@USER.COM",
            password="OMG_TESTS!"
        )
        
        self.auth_code = AuthCode()
        self.auth_code.save()
        
    def test_auth_code_generation(self):
        auth = AuthCode()
        auth.save()
        
        self.assertEqual(len(auth.code), CODE_LENGTH, "Saving the auth code should generate a code")
        
        
    def test_register_existing_username(self):
        existing_user_count = HMUser.objects.all().count()
        
        response = self.secure_post('/register', {
            'invite_code' : self.auth_code.code,
            'email' : 'test@user.com',
            'password' : 'test_password',
            'password_again' : 'test_password',
            'newsletter' : True
        })
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(existing_user_count + 1, HMUser.objects.all().count())
        
        
    def test_register_long_username(self):
        email = "T1234567890123456789012345678901234567@reallylongwebsitedomain.com.om"
        existing_user_count = HMUser.objects.all().count()
        
        response = self.secure_post('/register', {
            'invite_code' : self.auth_code.code,
            'email' : email,
            'password' : 'test_password',
            'password_again' : 'test_password',
            'newsletter' : True
        })
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(existing_user_count + 1, HMUser.objects.all().count())
        
        
    def test_register_invalid_auth_declines(self):
        existing_user_count = HMUser.objects.all().count()

        response = self.secure_post('/register', {
            'auth_code' : 'nocode',
            'email' : 'test_register_invalid_auth_declines@test.com',
            'password' : 'test_password',
            'password_again' : 'test_password'
        })
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(existing_user_count, HMUser.objects.all().count(), "Invalid auth code still created a user")
