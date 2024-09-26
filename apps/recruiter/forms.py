import random
import string
from django import forms
from django.forms import Select
from .models import MLO_AGENT


def generate_random_alphanumeric_strings(count=5, length=6):
    alphanumeric_chars = string.ascii_letters + string.digits
    return [''.join(random.choices(alphanumeric_chars, k=length)) for _ in range(count)][0]




class CustomSelect(Select):
    def __init__(self, attrs=None):
        default_attrs = {'class': 'custom-select-class'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs)



class MloFrom(forms.ModelForm):

    class Meta:
        CHOICES = [
        ('1', 'Choice 1'),
        ('2', 'Choice 2'),
        ('3', 'Choice 3'),
    ]
        model = MLO_AGENT
        exclude = "user",
        widgets = {
            'NMLS_sponsor_id': forms.TextInput(attrs={'maxlength':100,'readonly':True,"value":generate_random_alphanumeric_strings()}),
            'NMLS_ID': forms.TextInput(attrs={'maxlength':100,'readonly':True,"value":generate_random_alphanumeric_strings()}),
            "max"    : CustomSelect()

        }

    