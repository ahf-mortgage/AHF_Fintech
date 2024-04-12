from django.contrib import admin
from django import forms
from django.contrib import admin
from django.db import models
from .models import MLO,Loan,Company


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


admin.site.register(Loan)
