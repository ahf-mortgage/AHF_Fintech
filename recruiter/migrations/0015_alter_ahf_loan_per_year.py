# Generated by Django 5.0.4 on 2024-04-24 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0014_remove_loanbreakpoint_loan_per_month_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ahf',
            name='loan_per_year',
            field=models.IntegerField(default=1),
        ),
    ]