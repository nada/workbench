# Generated by Django 2.2.5 on 2019-09-15 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("services", "0003_auto_20190312_1535")]

    operations = [
        migrations.AlterField(
            model_name="servicetype",
            name="position",
            field=models.IntegerField(default=0, verbose_name="position"),
        )
    ]
