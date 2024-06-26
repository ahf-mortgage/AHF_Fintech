# Generated by Django 5.0.4 on 2024-04-25 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('W2branchYearlyGross', '0005_employeewithholdings_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='BranchPayrollLiabilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Social_Security', models.FloatField()),
                ('Medicare', models.FloatField()),
                ('Fed_Unemploy', models.FloatField()),
                ('Employment_Training_Tax', models.FloatField()),
                ('CA_Unemployment', models.FloatField()),
                ('total', models.FloatField()),
            ],
        ),
    ]
