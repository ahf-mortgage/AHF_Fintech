# Generated by Django 5.0.6 on 2024-06-08 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0014_rename_mlo_commision_mlo_agent_mlo_commission'),
    ]

    operations = [
        migrations.AddField(
            model_name='mlo_agent',
            name='year_to_date',
            field=models.FloatField(blank=True, null=True),
        ),
    ]