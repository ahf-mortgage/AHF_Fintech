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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the FloatField widget to readonly
        self.fields['gci'].widget.attrs['readonly'] = True


@admin.register(MLO)
class MLOAdmin(admin.ModelAdmin):
    form = MLOForm


# branch_commission= Branch.objects.all().first().commission
# @admin.register(AHF)
# class AHFAdmin(admin.ModelAdmin):
#     list_display = ['commission']
 
    # prepopulated_fields = {'commission':(1 - branch_commission,)},
    

admin.site.register(Loan)

admin.site.register(Bps)

admin.site.register(LoanBreakPoint)
admin.site.register(CompPlan)

# admin.site.register(AHF)
admin.site.register(Branch)
admin.site.register(AHF)


# calcuate ahf commission from branch commission by using formulae 1 - branch_commission



