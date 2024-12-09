# Generated by Django 5.1.3 on 2024-12-09 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kvs_app', '0021_alter_statecommitie_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statecommitie',
            name='position',
            field=models.CharField(blank=True, choices=[('president', 'State President'), ('secretary', 'Genaral Secretary'), ('treasurer', 'Treasurer'), ('vice_president', 'Vice President'), ('joint_secretary', 'Joint Secretary'), ('patron ', 'Patron '), ('legal_advisor', 'Legal Advisor '), ('working_committee', 'Working Committee')], default='working_committee', max_length=20, null=True),
        ),
    ]