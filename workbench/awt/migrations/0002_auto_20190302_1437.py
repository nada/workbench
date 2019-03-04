# Generated by Django 2.1.7 on 2019-03-02 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("awt", "0001_initial")]

    operations = [
        migrations.RemoveField(model_name="employment", name="vacation_days"),
        migrations.AddField(
            model_name="employment",
            name="vacation_weeks",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                help_text="Vacation weeks for a full year.",
                max_digits=4,
                verbose_name="vacation weeks",
            ),
            preserve_default=False,
        ),
    ]