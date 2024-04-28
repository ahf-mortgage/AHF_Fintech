from django import forms
from .models import BranchPayrollLiabilitiesQ

class BranchPayrollLiabilitiesQForm(forms.ModelForm):
    class Meta:
        model = BranchPayrollLiabilitiesQ
        fields = "value","Q_value"