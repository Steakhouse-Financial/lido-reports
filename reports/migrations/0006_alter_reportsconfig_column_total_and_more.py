# Generated by Django 4.1.7 on 2023-04-10 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0005_reportsources_reportsconfig_column_total_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reportsconfig",
            name="column_total",
            field=models.BooleanField(choices=[(True, "Yes"), (False, "No")]),
        ),
        migrations.AlterField(
            model_name="reportsconfig",
            name="field_chooser",
            field=models.BooleanField(choices=[(True, "Yes"), (False, "No")]),
        ),
        migrations.AlterField(
            model_name="reportsconfig",
            name="row_total",
            field=models.BooleanField(choices=[(True, "Yes"), (False, "No")]),
        ),
        migrations.AlterField(
            model_name="reportsconfig",
            name="show_account",
            field=models.CharField(
                blank=True,
                choices=[("YES", "Yes"), ("NO", "No")],
                default=None,
                max_length=3,
            ),
        ),
        migrations.AlterField(
            model_name="reportsconfig",
            name="show_category",
            field=models.CharField(
                blank=True,
                choices=[("YES", "Yes"), ("NO", "No")],
                default=None,
                max_length=3,
            ),
        ),
        migrations.AlterField(
            model_name="reportsconfig",
            name="show_primary",
            field=models.CharField(
                blank=True,
                choices=[("YES", "Yes"), ("NO", "No")],
                default=None,
                max_length=3,
            ),
        ),
        migrations.AlterField(
            model_name="reportsconfig",
            name="show_secondary",
            field=models.CharField(
                blank=True,
                choices=[("YES", "Yes"), ("NO", "No")],
                default=None,
                max_length=3,
            ),
        ),
        migrations.AlterField(
            model_name="reportsconfig",
            name="show_subcategory",
            field=models.CharField(
                blank=True,
                choices=[("YES", "Yes"), ("NO", "No")],
                default=None,
                max_length=3,
            ),
        ),
    ]