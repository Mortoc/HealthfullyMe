from django.contrib import admin
from home.models import EmailRequest
from home.models import AuthCode

class AuthCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'uses_left')
    readonly_fields = ('code', 'created_date', 'registered_users')
    
admin.site.register(AuthCode, AuthCodeAdmin)


class EmailRequestAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_date')
    

admin.site.register(EmailRequest, EmailRequestAdmin)