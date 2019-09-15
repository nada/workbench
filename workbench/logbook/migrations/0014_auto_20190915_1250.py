# Generated by Django 2.2.5 on 2019-09-15 10:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("logbook", "0013_auto_20190915_1222")]

    operations = [
        migrations.AlterField(
            model_name="loggedcost",
            name="service",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="loggedcosts",
                to="projects.Service",
                verbose_name="service",
            ),
        )
    ]
