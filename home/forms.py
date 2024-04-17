from django import forms
from ..recruiter.models import CompPlan


class CompPlanInputForm(forms.ModelForm):
    class Meta:
        model  = CompPlan
        fields = "__all__"