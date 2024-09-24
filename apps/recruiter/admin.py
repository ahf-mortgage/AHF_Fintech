from django.contrib import admin
from django import forms
from django.contrib import admin
from django.db import models
from .models import *


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the FloatField widget to readonly
        self.fields['total'].widget.attrs['readonly'] = True


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    form = CompanyForm


class MLOForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'




@admin.register(MLO)
class MLOAdmin(admin.ModelAdmin):
    form = MLOForm



@admin.register(Loan)
class MLOAdmin(admin.ModelAdmin):
    search_fields = 'mlo_agent__user__username',

@admin.register(LoanAmount)
class MLOAdmin(admin.ModelAdmin):
    search_fields = 'File_reference',"loan_amount"




@admin.register(Edge)
class MLOAdmin(admin.ModelAdmin):
    search_fields = 'source_node__user__username',"target_node__user__username"

admin.site.register(Bps)


admin.site.register(LoanBreakPoint)
admin.site.register(CompPlan)

admin.site.register(AHF)
admin.site.register(Recruiter)
admin.site.register(Branch)
admin.site.register(Node)
admin.site.register(LoanSetting)
admin.site.register(MLO_AGENT)


