# Generated by Django 5.0.4 on 2024-04-14 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0006_bps'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanBreakPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_break_point', models.FloatField()),
            ],
        ),
    ]