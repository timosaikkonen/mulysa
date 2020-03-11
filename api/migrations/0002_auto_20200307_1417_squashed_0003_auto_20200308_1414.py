# Generated by Django 3.0.3 on 2020-03-08 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [("api", "0002_auto_20200307_1417"), ("api", "0003_auto_20200308_1414")]

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accessdevice",
            name="deviceid",
            field=models.CharField(
                help_text="used to know which device this was",
                max_length=255,
                unique=False,
                verbose_name="device id",
            ),
        ),
        migrations.AlterField(
            model_name="accessdevice",
            name="deviceid",
            field=models.CharField(
                help_text="used to know which device this was",
                max_length=512,
                unique=True,
                verbose_name="device id",
            ),
        ),
    ]
