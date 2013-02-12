from django.db import models
from django import forms
from django.utils import timezone
from django.contrib import admin


class EmailRequest(models.Model):
    email = models.EmailField()
    created_date = models.DateTimeField(default=timezone.now())


class EmailRequestForm(forms.Form):
    email = forms.EmailField()


class EmailRequestAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_date')
        

admin.site.register(EmailRequest, EmailRequestAdmin)