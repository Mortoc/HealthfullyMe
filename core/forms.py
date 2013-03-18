from django import forms
from core.models import HMUser

class SetPasswordForm(forms.Form):
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())
    password_again = forms.CharField(max_length=30, widget=forms.PasswordInput())
    
    def clean(self):
        cleaned_data = super(SetPasswordForm, self).clean()
        
        if cleaned_data.get("password") != cleaned_data.get("password_again"):
            self._errors["password"] = self.error_class(["Passwords must match"])
            self._errors["password_again"] = self.error_class(["Passwords must match"])
        
        return cleaned_data
    