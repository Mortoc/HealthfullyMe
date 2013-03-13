from django.contrib import admin
from home.models import EmailRequest
from home.models import AuthCode

class AuthCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'uses_left')
    fieldsets = [
        (None,               {'fields': ['code', 'uses_left', 'created_date']}),
        ('Registered Users', {'fields': ['registered_users'], 'classes': ['collapse']}),
    ]
    readonly_fields = ('code', 'created_date', 'registered_users')
    
admin.site.register(AuthCode, AuthCodeAdmin)


class EmailRequestAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_date_in_EST')
    

admin.site.register(EmailRequest, EmailRequestAdmin)