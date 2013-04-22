from django.utils import unittest
from django.test import TestCase
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from store.models import Transaction, Offer, OfferAvailability
from store.views import record_charge_ajax

from core.models import HMUser
from core.test.TestCasePlus import TestCasePlus
import json
import stripe

class TransactionTest(TestCasePlus):
    def setUp(self):
        super(TransactionTest, self).setUp()
        
        self.test_user = HMUser.objects.create_user (
            email = "TEST@USER.COM".lower(), 
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
        
    def generate_mock_charge(self):
        charge = stripe.Charge()
        card = stripe.Customer()
        charge.id = "some_crazyID2350894735"
        charge.card = card
        card.name = "TEST_USER"
        card.address_line1 = "Somewhere"
        card.address_line2 = "Over the rainbow"
        card.address_city = "Way up high"
        card.address_zip = "12345"
        card.address_state = "NY"
        card.address_country = "USA"
        card.fingerprint = "test_fingerprint"
        card.last4 = "1234"
        card.exp_month = 12
        card.exp_year = 2034
        card.type = "Visa"
        
        return charge
    
    def mock_run_stripe_charge(self, price, stripe_token, email):
        self.assertEqual(price, self.test_offer.price)
        self.assertEqual(stripe_token, "test_token")
        self.assertEqual(email.lower(), "TEST@USER.COM".lower())
        
        return self.generate_mock_charge()
    
    def mock_run_stripe_charge_failure(self, price, stripe_token, email):
        self.assertEqual(price, self.test_offer.price)
        self.assertEqual(stripe_token, "test_token")
        self.assertEqual(email.lower(), "TEST@USER.COM".lower())
        
        raise stripe.CardError("TEST ERROR", "failed", "123", "200")
    
    def mock_run_stripe_charge_server_error(self, price, stripe_token, username):
        raise Exception("Fake Server Error")
    
    def test_offer_availability_limits(self):        
        request = self.get_secure_request('/store/record-charge')
        request.user = HMUser.objects.get(email=self.test_user.email)
        request.method = "POST"
        
        new_rule = OfferAvailability(time_value=1, time_peroid=3) # 1 month
        new_rule.save()
        self.test_offer.availability.add( new_rule )
        self.test_offer.save()
        
        request.POST = {
            'offer_id' : str(self.test_offer.id),
            'stripe_token' : "test_token"
        }
        
        # First try should be successful
        response = record_charge_ajax(
            request, 
            self.mock_run_stripe_charge
        )
        response_content = json.loads( response.content )
        self.assertEqual( response_content['status'] ,"success" )
        self.assertEqual( response.status_code, 200 )
        
        request.user = HMUser.objects.get(email=self.test_user.email)
        
        # Second try should fail
        response = record_charge_ajax(
            request, 
            self.mock_run_stripe_charge
        )
        response_content = json.loads( response.content )
        self.assertEqual(response_content['status'], 'not-available')
        self.assertEqual(response.status_code, 200)
        
    def test_logged_in_user_can_access_store_page(self):
        self.do_login(self.test_user.email, self.test_user.password)
        
        self.assertTrue( self.test_user.is_authenticated )
        
        response = self.secure_get('/store')
        
        self.assertEqual(response.status_code, 200)
        
        # check for a random bit of content that would be in the 
        #  correctly-rendered page
        self.assertTrue( settings.SEGMENT_IO_KEY in str(response) )
        
    
    def test_record_charge_ajax_on_successful_card(self):
        request = self.get_secure_request('/store/record-charge')
        request.user = self.test_user
        request.method = "POST"
        request.POST = {
            'offer_id' : str(self.test_offer.id),
            'stripe_token' : "test_token"
        }
        
        response = record_charge_ajax(
            request, 
            self.mock_run_stripe_charge
        )
        
        response_content = json.loads( response.content )
        
        self.assertEqual( response_content['status'] ,"success" )
        self.assertEqual( response.status_code, 200 )


    def test_record_charge_ajax_error_handling(self):
        request = self.get_secure_request('/store/record-charge')
        request.user = self.test_user
        request.method = "POST"
        request.POST = {
            'offer_id' : str(self.test_offer.id),
            'stripe_token' : "test_token"
        }
        
        response = record_charge_ajax(
            request, 
            self.mock_run_stripe_charge_failure
        )
        
        response_content = json.loads( response.content )
        
        self.assertEqual(response_content['status'], 'card-declined')
        self.assertEqual(response_content['message'], 'failed')
        self.assertEqual(response.status_code, 200)
        
        response = record_charge_ajax(
            request,
            self.mock_run_stripe_charge_server_error
        )
        
        response_content = json.loads( response.content )
        
        self.assertEqual(response_content['status'], 'server-error')
        self.assertTrue(len(response_content['message']) > 0)
        self.assertEqual(response.status_code, 200)
