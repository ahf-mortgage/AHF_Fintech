# forms.py
from django import forms
from .models import MLO

class MLOForm(forms.ModelForm):
    class Meta:
        model = MLO
        fields = "__all__"