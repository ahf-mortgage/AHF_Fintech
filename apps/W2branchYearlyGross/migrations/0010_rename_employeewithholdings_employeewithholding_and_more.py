# Generated by Django 5.0.4 on 2024-04-28 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('W2branchYearlyGross', '0009_alter_branchpayrollliabilities_ca_unemployment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EmployeeWithHoldings',
            new_name='EmployeeWithholding',
        ),
        migrations.AlterField(
            model_name='branchpayrollliabilities',
            name='Social_Security',
            field=models.FloatField(verbose_name='Social Security'),
        ),
    ]
