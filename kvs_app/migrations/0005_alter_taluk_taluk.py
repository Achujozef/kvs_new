# Generated by Django 4.2.7 on 2024-09-28 05:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kvs_app", "0004_join_kvs_data_enter_by_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="taluk",
            name="taluk",
            field=models.CharField(max_length=50),
        ),
    ]
