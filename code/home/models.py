from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from core.base62encode import base62_encode
from django.contrib.auth.models import User
import random
import math

class EmailRequest(models.Model):
    email = models.EmailField()
    created_date = models.DateTimeField(default=timezone.now())
    

MAX_CODE_LENGTH = 5
class AuthCode(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.SlugField(max_length=MAX_CODE_LENGTH)
    uses_left = models.IntegerField(default=1)
    created_date = models.DateTimeField(default=timezone.now())
    registered_users = models.ManyToManyField( User )
    
    def generate_code(self):
        # we want to get a value that uses all 5 digits of the base-62 encoded string
        maxCodeValue = math.pow(62, MAX_CODE_LENGTH)
        minCodeValue = math.pow(62, MAX_CODE_LENGTH - 1)
        
        self.code = base62_encode( random.randint(minCodeValue, maxCodeValue) )
        self.save()
        

def model_created(sender, **kwargs):
    auth_code_instance = kwargs['instance']
    if kwargs['created']:
        auth_code_instance.generate_code()

post_save.connect(model_created, sender=AuthCode)
