# Generated by Django 5.0.4 on 2024-04-28 17:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('W2branchYearlyGross', '0014_branchpayrollliabilitiesq_bpql'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchpayrollliabilitiesq',
            name='bpql',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='W2branchYearlyGross.branchpayrollliabilities'),
        ),
    ]
