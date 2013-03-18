from django import forms
from core.models import HMUser

class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())
    
    def clean(self):
        cleaned_data = super(UserLoginForm, self).clean()
        
        email_string = cleaned_data.get("email")
        
        if email_string != None:
            cleaned_data["email"] = email_string.lower()
        else:
            self._errors['email'] = self.error_class(["Invalid Email"])
        
        return cleaned_data

class UserRegistrationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())
    password_again = forms.CharField(max_length=30, widget=forms.PasswordInput())
    invite_code = forms.CharField(max_length=30)
    newsletter = forms.BooleanField(label="Receive the newsletter", initial=True)
    
    def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        
        email_string = cleaned_data.get("email")
        if email_string != None:
            cleaned_data["email"] = email_string.lower()
        else:
            self._errors['email'] = self.error_class(["Invalid Email"])
        
        if cleaned_data.get("password") != cleaned_data.get("password_again"):
            self._errors["password"] = self.error_class(["Passwords must match"])
            self._errors["password_again"] = self.error_class(["Passwords must match"])
        
        user_exists = True
        try:
            HMUser.objects.get(email = cleaned_data.get("email"))
        except HMUser.DoesNotExist:
            user_exists = False
            
        if user_exists:
            self._errors["email"] = self.error_class(["That Email is already registered"])
        
        return cleaned_data
    
    
class EmailRequestForm(forms.Form):
    email = forms.EmailField()
