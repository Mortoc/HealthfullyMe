from django.db import models
from django.db.models.signals import post_save
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.conf import settings

from core.timeutil import show_time_as
from core.encode import base62_encode

import random
import math

class EmailRequest(models.Model):
    email = models.EmailField()
    created_date = models.DateTimeField(default=now)
    code_sent = models.BooleanField(default=False)
    
    def created_date_in_EST(self):
        return show_time_as(self.created_date, 'America/New_York')
    
    

CODE_LENGTH = 5
class AuthCode(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.SlugField(max_length=CODE_LENGTH)
    uses_left = models.IntegerField(default=1)
    created_date = models.DateTimeField(default=now)
    registered_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    notes = models.TextField(default=" ")
    
    def generate_code(self):
        # we want to get a value that uses all 5 digits of the base-62 encoded string
        max_code = math.pow(62, CODE_LENGTH)
        min_code = math.pow(62, CODE_LENGTH - 1)
        
        self.code = base62_encode( random.randint(min_code, max_code) )
        self.save()
        

def model_created(sender, **kwargs):
    auth_code_instance = kwargs['instance']
    if kwargs['created']:
        auth_code_instance.generate_code()

post_save.connect(model_created, sender=AuthCode)
