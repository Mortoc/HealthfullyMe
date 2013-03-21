from django.contrib import admin
from home.models import EmailRequest
from home.models import AuthCode

class AuthCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'uses_left')
    fieldsets = [
        (None,               {'fields': ['code', 'uses_left', 'notes', 'created_date']}),
        ('Registered Users', {'fields': ['registered_users'], 'classes': ['collapse']}),
    ]
    readonly_fields = ('code', 'created_date', 'registered_users')
    
admin.site.register(AuthCode, AuthCodeAdmin)


class EmailRequestAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_date_in_EST', 'code_sent')
    

admin.site.register(EmailRequest, EmailRequestAdmin)