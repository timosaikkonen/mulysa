# Generated by Django 3.0.3 on 2020-02-24 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_custominvoice"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="birthday",
            field=models.DateField(verbose_name="Birthday"),
        ),
    ]
