# Generated by Django 4.2.7 on 2024-09-28 05:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kvs_app", "0005_alter_taluk_taluk"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sakha",
            name="taluk",
            field=models.CharField(max_length=50),
        ),
    ]