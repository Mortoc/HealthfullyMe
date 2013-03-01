from django.utils import unittest
from django.test.client import RequestFactory
from django.test import TestCase

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from store.models import Transaction, Offer
from store.views import record_charge_ajax
import stripe

class TransactionTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        
        self.test_user = User.objects.create_user (
            username = "TEST_USER", 
            email = "TEST@USER.COM", 
            password = "OMG_TESTS!"
        )
        
        self.test_offer = Offer(
            header_text = "Test Offer",
            description_line_1 = "Test Line 1",
            description_line_2 = "Test Line 2",
            description_line_3 = "Test Line 3",
            description_line_4 = "Test Line 4",
            description_line_5 = "Test Line 5",
            buy_window_title = "Test Window Title",
            buy_window_description = "Test Window Description",
            price = 1234,
            enabled = True
        )
        self.test_offer.save()
        
        
    def test_id_slug_generation(self):
        pass;
    
    
    def mock_run_stripe_charge(self, price, stripe_token, username):
        self.assertEqual(price, self.test_offer.price)
        self.assertEqual(stripe_token, "test_token")
        self.assertEqual(username, "TEST_USER")
    
    def mock_run_stripe_charge_failure(self, price, stripe_token, username):
        self.assertEqual(price, self.test_offer.price)
        self.assertEqual(stripe_token, "test_token")
        self.assertEqual(username, "TEST_USER")
        
        raise stripe.CardError("TEST ERROR", "failed", "123", "200")
    
    
    def test_record_charge_ajax_on_successful_card(self):
        request = self.factory.get('/store/record-charge')
        request.user = self.test_user
        request.method = "POST"
        request.POST = {
            'offer_id' : str(self.test_offer.id),
            'stripe_token' : "test_token"
        }
        
        response = record_charge_ajax (
            request, 
            self.mock_run_stripe_charge
        )
        
        self.assertEqual(response.content ,"\"success\"")
        self.assertEqual(response.status_code, 200)


    def test_record_charge_ajax_on_failed_card(self):
        request = self.factory.get('/store/record-charge')
        request.user = self.test_user
        request.method = "POST"
        request.POST = {
            'offer_id' : str(self.test_offer.id),
            'stripe_token' : "test_token"
        }
        
        response = record_charge_ajax (
            request, 
            self.mock_run_stripe_charge_failure
        )
        
        self.assertEqual(response.content, '\"card-declined\"')
        self.assertEqual(response.status_code, 200)
