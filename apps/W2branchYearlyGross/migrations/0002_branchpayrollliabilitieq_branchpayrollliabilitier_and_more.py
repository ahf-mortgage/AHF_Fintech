# Generated by Django 4.2.2 on 2024-07-28 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("W2branchYearlyGross", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BranchPayrollLiabilitieQ",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Social_Security", models.FloatField(verbose_name="Social Security")),
                ("Medicare", models.FloatField()),
                ("Fed_Unemploy", models.FloatField()),
                ("CA_Unemployment", models.FloatField(verbose_name="CA Unemployment")),
                (
                    "Employment_Training_Tax",
                    models.FloatField(verbose_name="Employment Training Tax (ETT)"),
                ),
                ("total", models.FloatField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Branch Payroll Liabilities Q column",
                "verbose_name_plural": "Branch Payroll Liabilities Q column",
            },
        ),
        migrations.CreateModel(
            name="BranchPayrollLiabilitieR",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Social_Security", models.FloatField(verbose_name="Social Security")),
                ("Medicare", models.FloatField()),
                ("Fed_Unemploy", models.FloatField()),
                ("CA_Unemployment", models.FloatField(verbose_name="CA Unemployment")),
                (
                    "Employment_Training_Tax",
                    models.FloatField(verbose_name="Employment Training Tax (ETT)"),
                ),
                ("total", models.FloatField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Branch Payroll Liabilities R column",
                "verbose_name_plural": "Branch Payroll Liabilities R column",
            },
        ),
        migrations.CreateModel(
            name="BranchPayrollLiabilities",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Social_Security", models.FloatField(verbose_name="Social Security")),
                ("Medicare", models.FloatField()),
                ("Fed_Unemploy", models.FloatField()),
                ("CA_Unemployment", models.FloatField(verbose_name="CA Unemployment")),
                (
                    "Employment_Training_Tax",
                    models.FloatField(verbose_name="Employment Training Tax (ETT)"),
                ),
                ("total", models.FloatField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Branch Payroll Liabilities",
                "verbose_name_plural": "Branch Payroll Liabilities",
            },
        ),
        migrations.CreateModel(
            name="EmployeeWithholding",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Social_Security", models.FloatField()),
                ("Medicare", models.FloatField()),
                ("CA_disability", models.FloatField()),
                ("total", models.FloatField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Employee Withholding",
                "verbose_name_plural": "Employee Withholding",
            },
        ),
        migrations.CreateModel(
            name="EmployeeWithholdingQ",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Social_Security", models.FloatField()),
                ("Medicare", models.FloatField()),
                ("CA_disability", models.FloatField()),
                ("total", models.FloatField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Employee Withholding Q column",
                "verbose_name_plural": "Employee Withholding R column",
            },
        ),
        migrations.CreateModel(
            name="EmployeeWithholdingR",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Social_Security", models.FloatField()),
                ("Medicare", models.FloatField()),
                ("CA_disability", models.FloatField()),
                ("total", models.FloatField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Employee Withholding R column",
                "verbose_name_plural": "Employee Withholding R column",
            },
        ),
        migrations.CreateModel(
            name="Q22",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("value", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="Expense",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("expense", models.FloatField()),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="expense",
                        to="W2branchYearlyGross.category",
                    ),
                ),
            ],
        ),
    ]