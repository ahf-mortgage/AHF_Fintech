# Generated by Django 4.2.2 on 2024-08-01 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recruiter", "0006_remove_loanamount_recruiter_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="loan",
            name="bps",
            field=models.FloatField(default=2.75),
            preserve_default=False,
        ),
    ]