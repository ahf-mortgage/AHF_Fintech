# Generated by Django 5.0.4 on 2024-05-07 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('W2branchYearlyGross', '0019_employeewithholdingq_employeewithholdingr'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branchpayrollliabilitieq',
            options={'verbose_name': 'Branch Payroll Liabilities Q column', 'verbose_name_plural': 'Branch Payroll Liabilities Q column'},
        ),
        migrations.AlterModelOptions(
            name='branchpayrollliabilitier',
            options={'verbose_name': 'Branch Payroll Liabilities R column', 'verbose_name_plural': 'Branch Payroll Liabilities R column'},
        ),
        migrations.AlterModelOptions(
            name='branchpayrollliabilities',
            options={'verbose_name': 'Branch Payroll Liabilities', 'verbose_name_plural': 'Branch Payroll Liabilities'},
        ),
        migrations.AlterModelOptions(
            name='employeewithholdingq',
            options={'verbose_name': 'Employee Withholding Q column', 'verbose_name_plural': 'Employee Withholding R column'},
        ),
        migrations.AlterModelOptions(
            name='employeewithholdingr',
            options={'verbose_name': 'Employee Withholding R column', 'verbose_name_plural': 'Employee Withholding R column'},
        ),
    ]