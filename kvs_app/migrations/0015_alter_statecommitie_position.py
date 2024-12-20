# Generated by Django 5.1.3 on 2024-12-04 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kvs_app', '0014_statecommitie_position_alter_databank_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statecommitie',
            name='position',
            field=models.CharField(blank=True, choices=[('president', 'State President'), ('secretary', 'Genaral Secretary'), ('treasurer', 'Treasurer'), ('vice_president', 'Vice President'), ('joint_secretary', 'Joint Secretary'), ('working_committee', 'Working Committee')], default='working_committee', max_length=20, null=True),
        ),
    ]
