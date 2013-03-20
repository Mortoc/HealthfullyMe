from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from core.models import HMUser, Address


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = HMUser
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

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
    readonly_fields = ('created_date', 'logins', 'password_admin_reset', 'receives_newsletter',)
    filter_horizontal = ()

admin.site.register(HMUser, HMUserAdmin)
admin.site.register(Address)

