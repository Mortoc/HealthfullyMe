from django.db import models
from django import forms
from django.utils import timezone

class EmailRequest(models.Model):
    email = models.EmailField()
    created_date = models.DateTimeField(default=timezone.now())


class EmailRequestForm(forms.Form):
    email = forms.EmailField()

