# Generated by Django 4.2.2 on 2024-07-28 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("recruiter", "0003_remove_loan_amount_loan_amount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="loan",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="recruiter.mlo_agent",
            ),
        ),
    ]