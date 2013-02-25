from django import forms
from django.contrib.auth.models import User

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
    auth_code = forms.CharField(max_length=30)
    
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
            User.objects.get(username = cleaned_data.get("email"))
        except User.DoesNotExist:
            user_exists = False
            
        if user_exists:
            self._errors["email"] = self.error_class(["That Email is already registered"])
            
        print "Cleaning UserRegistrationForm"
        
        return cleaned_data
    
    
class EmailRequestForm(forms.Form):
    email = forms.EmailField()