from django import forms

class EmailRequest(forms.Form):
    email = forms.EmailField()        