from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from core.models import HMUser, Address, Tag

class HMUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_date', 'is_admin',)
    list_filter = ('is_admin', 'created_date',)
    fieldsets = (
        (None, {'fields': ('email', 'password_admin_reset', 'first_name', 'last_name', 'created_date', 'receives_newsletter',)}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_legacy', )}),
        ('Logins', {'fields': ('logins',), 'classes': ['collapse']}),
    )
    search_fields = ('email',)
    ordering = ('email', 'created_date',)
    readonly_fields = ('created_date', 'logins', 'password_admin_reset',)

admin.site.register(HMUser, HMUserAdmin)
admin.site.register(Address)
admin.site.register(Tag)

admin.site.unregister(Group)

