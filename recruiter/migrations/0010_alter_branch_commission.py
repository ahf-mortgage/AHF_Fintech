# Generated by Django 5.0.4 on 2024-04-14 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0009_ahf_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='commission',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]