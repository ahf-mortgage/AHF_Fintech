# Generated by Django 5.0.4 on 2024-04-28 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('W2branchYearlyGross', '0008_alter_branchpayrollliabilities_employment_training_tax'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchpayrollliabilities',
            name='CA_Unemployment',
            field=models.FloatField(verbose_name='CA Unemployment'),
        ),
    ]
