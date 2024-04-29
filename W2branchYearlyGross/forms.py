from django import forms
from .models import BranchPayrollLiabilitieQ

class BranchPayrollLiabilitiesQForm(forms.ModelForm):
    class Meta:
        model = BranchPayrollLiabilitieQ
        fields = "__all__"