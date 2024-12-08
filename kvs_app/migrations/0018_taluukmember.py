# Generated by Django 5.1.3 on 2024-12-08 13:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kvs_app', '0017_sakhamember'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaluukMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('position', models.CharField(choices=[('President', 'President'), ('Secretary', 'Secretary'), ('Treasurer', 'Treasurer')], max_length=20)),
                ('taluk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='kvs_app.taluk')),
            ],
        ),
    ]
