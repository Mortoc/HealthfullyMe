from django.utils import unittest
from django.test.client import RequestFactory
from django.test import TestCase
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import AnonymousUser

from home.views import login_user, logout_user
from core.models import *
from core.test.TestCasePlus import TestCasePlus

class MockSession(dict):
    def __init__(self):
        self._dict = {}

    def add(self, id, val):
        self._dict[id] = val
        
    def cycle_key(self):
        pass
    
    def set_test_cookie(self):
        pass
    
class HMUserVerification(TestCasePlus):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        
        self.test_user = HMUser.objects.create_user (
            email="TEST@USER.COM".lower(),
            password="OMG_TESTS!"
        )
        
        self.test_user.save()
        
    def do_login(self, email, password):
        return self.secure_post('/login', {
            'email' : email,
            'password' : password,
        })
        
    def test_admins_are_autmatically_made_staff(self):
        self.test_user.is_admin = True
        self.test_user.is_staff = False
        self.test_user.save()

        self.assertEqual(self.test_user.is_staff, True)
        
        
    def test_logins_are_recorded(self):
        initial_logins = self.test_user.logins.count()

        self.do_login('test@user.com', 'OMG_TESTS!')
        self.assertEqual(initial_logins + 1, HMUser.objects.get(email = 'test@user.com').logins.count(), "Logging in didn't increment the logins count")
        
        self.do_login('test@user.com', 'THIS IS THE WRONG PASSWORD')
        self.assertEqual(initial_logins + 1, HMUser.objects.get(email = 'test@user.com').logins.count(), "Failed login still incremented the logins count")
        
    def test_set_new_password(self):
        first_password = "OMG_TESTS_NEW!"
        second_password = "ERMAGHAD_TERSTS!"
        
        initial_logins = HMUser.objects.get(email = 'test@user.com').logins.count()
        
        self.test_user.set_password(first_password)
        self.test_user.save()
        self.do_login('test@user.com', first_password)
        self.assertEqual(HMUser.objects.get(email = 'test@user.com').logins.count(), initial_logins + 1, "Logging in after setting a new password failed")
        
        self.test_user.set_password(second_password)
        self.test_user.save()
        self.do_login('test@user.com', first_password) #login with the wrong password, make sure it doesn't work
        self.assertEqual(HMUser.objects.get(email = 'test@user.com').logins.count(), initial_logins + 1, "Failed login after setting a new password still incremented logins count")
        
        self.do_login('test@user.com', second_password)
        self.assertEqual(HMUser.objects.get(email = 'test@user.com').logins.count(), initial_logins + 2, "Setting a new password didn't work")
        
        self.test_user.set_password(first_password)
        self.test_user.save()
        self.do_login('test@user.com', first_password)
        self.assertEqual(HMUser.objects.get(email = 'test@user.com').logins.count(), initial_logins + 3, "Setting back to an earlier password didn't work")
        
        
