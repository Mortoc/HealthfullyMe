from django.contrib import admin
from home.models import EmailRequest


class EmailRequestAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_date')
        

admin.site.register(EmailRequest, EmailRequestAdmin)