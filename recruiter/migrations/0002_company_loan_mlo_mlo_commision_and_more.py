# Generated by Django 5.0.4 on 2024-04-12 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('cap', models.FloatField()),
                ('company_commission', models.FloatField()),
                ('total', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='mlo',
            name='MLO_commision',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlo',
            name='annual_commision_paid_to_company',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlo',
            name='break_point',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlo',
            name='comp',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mlo',
            name='date_joined',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='mlo',
            name='gci',
            field=models.FloatField(blank=True, null=True),
        ),
    ]