# Generated by Django 4.2 on 2024-05-23 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0008_remove_mlo_mlo_commision_remove_mlo_nmls_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recruiter',
            old_name='level',
            new_name='amount',
        ),
    ]