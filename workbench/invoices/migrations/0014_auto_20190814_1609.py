# Generated by Django 2.2.4 on 2019-08-14 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("invoices", "0013_auto_20190630_2220")]

    operations = [
        migrations.AddField(
            model_name="invoice",
            name="show_service_details",
            field=models.BooleanField(
                default=True, verbose_name="show service details"
            ),
        ),
        migrations.AddField(
            model_name="recurringinvoice",
            name="show_service_details",
            field=models.BooleanField(
                default=True, verbose_name="show service details"
            ),
        ),
    ]
