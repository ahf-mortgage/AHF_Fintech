# Generated by Django 5.0.4 on 2024-04-14 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0005_wholesalelendercompplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bps', models.FloatField()),
            ],
        ),
    ]