# Generated by Django 4.1.7 on 2023-04-10 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0006_alter_reportsconfig_column_total_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="reportsconfig",
            name="source_table",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="reports.reportsources",
            ),
            preserve_default=False,
        ),
    ]