from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django import forms
import string

class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())
    
    def clean(self):
        cleaned_data = super(UserLoginForm, self).clean()
        
        cleaned_data["email"] = cleaned_data.get("email").lower()
        
        try:
            User.objects.get(username=cleaned_data.get("email"))
        except User.DoesNotExist:
            raise forms.ValidationError("User does not exist")
        
        return cleaned_data
            

class UserRegistrationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())
    password_again = forms.CharField(max_length=30, widget=forms.PasswordInput())
    auth_code = forms.CharField(max_length=30)
    
    def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        
        cleaned_data["email"] = cleaned_data.get("email").lower()
        
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
            
        if cleaned_data.get('auth_code') != '12345':
            self._errors['auth_code'] = self.error_class(["Invalid Code"])
            
        print "Cleaning UserRegistrationForm"
        
        return cleaned_data
    

def login_user(request):
    if request.user.is_authenticated():
        HttpResponseRedirect('/store/')
    
    if request.method == 'POST': 
        
        form = UserLoginForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = authenticate(username = email, password = password)
            
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = UserLoginForm()
        
    return render_to_response (
            'login.html', 
            { 'form': form },
            context_instance = RequestContext(request)
        )
    
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
    
def register_user(request):
    if request.user.is_authenticated():
        HttpResponseRedirect('/store/')
        
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            print "username: " + username + "\npassword: " + password
            
            user = User.objects.create_user(username = username, email = username, password = password)
            user.save()
            
            login(request, authenticate(username = username, password = password))
            
            return HttpResponseRedirect('/')
    else:
        form = UserRegistrationForm()
             
    return render_to_response (
            'register.html', 
            { 'form': form },
            context_instance = RequestContext(request)
        )
