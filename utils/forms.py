from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import PrependedText
from django import forms
from allauth.account.forms import SignupForm



class AHFSignupForm(SignupForm):
    email = forms.EmailField(widget=forms.EmailInput())
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    
 
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password1')
        # self.fields['password1'].widget.attrs['aria-describedby'] = ''
        self.fields['password2'].widget.attrs['aria-describedby'] = ''
