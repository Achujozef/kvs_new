# Generated by Django 4.1 on 2024-09-01 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DataBankCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'DATA BANK CATEGORY',
            },
        ),
        migrations.CreateModel(
            name='Gender_choices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name_plural': 'Add Gender',
            },
        ),
        migrations.CreateModel(
            name='Id_details_choices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Add Id card choices',
            },
        ),
        migrations.CreateModel(
            name='Insurence_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Add Insurence category',
            },
        ),
        migrations.CreateModel(
            name='Payment_details_choices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Add Payment Details choices',
            },
        ),
        migrations.CreateModel(
            name='Sex_Choices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'verbose_name_plural': 'Add Sex',
            },
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name_plural': 'Add Star',
            },
        ),
        migrations.CreateModel(
            name='StateCommitie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('place', models.CharField(max_length=250)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='state commitie')),
            ],
            options={
                'verbose_name_plural': 'State Commitie',
            },
        ),
        migrations.CreateModel(
            name='SubCaste_choices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name_plural': 'Add Subcaste',
            },
        ),
        migrations.CreateModel(
            name='Taluk_choices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Add Union',
            },
        ),
        migrations.CreateModel(
            name='Taluk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('district', models.CharField(choices=[('Trivandrum', 'Trivandrum'), ('Kollam', 'Kollam'), ('Pathanamthitta', 'Pathanamthitta'), ('Alappuzha', 'Alappuzha'), ('Kottayam', 'Kottayam'), ('Idukki', 'Idukki'), ('Ernakulam', 'Ernakulam'), ('Thrissur', 'Thrissur'), ('Palakkad', 'Palakkad'), ('Malappuram', 'Malappuram'), ('Kozhikode', 'Kozhikode'), ('Wayanad', 'Wayanad'), ('Kannur', 'Kannur'), ('Kasaragod', 'Kasaragod')], max_length=50)),
                ('taluk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kvs_app.taluk_choices')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('mobile_no', models.CharField(max_length=10)),
                ('joining_date', models.DateField(blank=True, null=True)),
                ('id_no', models.CharField(max_length=25)),
                ('sakha_no', models.CharField(max_length=25)),
                ('district', models.CharField(choices=[('Trivandrum', 'Trivandrum'), ('Kollam', 'Kollam'), ('Pathanamthitta', 'Pathanamthitta'), ('Alappuzha', 'Alappuzha'), ('Kottayam', 'Kottayam'), ('Idukki', 'Idukki'), ('Ernakulam', 'Ernakulam'), ('Thrissur', 'Thrissur'), ('Palakkad', 'Palakkad'), ('Malappuram', 'Malappuram'), ('Kozhikode', 'Kozhikode'), ('Wayanad', 'Wayanad'), ('Kannur', 'Kannur'), ('Kasaragod', 'Kasaragod')], max_length=50)),
                ('taluk', models.CharField(max_length=25)),
                ('proposed_by_name', models.CharField(blank=True, max_length=25, null=True)),
                ('proposed_by_contact_no', models.CharField(blank=True, max_length=25, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=25)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kvs_app.insurence_category')),
                ('id_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kvs_app.id_details_choices')),
                ('payment_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kvs_app.payment_details_choices')),
            ],
            options={
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Sakha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sakha_no', models.CharField(max_length=50)),
                ('sakaha_name', models.CharField(blank=True, max_length=50, null=True)),
                ('district', models.CharField(choices=[('Trivandrum', 'Trivandrum'), ('Kollam', 'Kollam'), ('Pathanamthitta', 'Pathanamthitta'), ('Alappuzha', 'Alappuzha'), ('Kottayam', 'Kottayam'), ('Idukki', 'Idukki'), ('Ernakulam', 'Ernakulam'), ('Thrissur', 'Thrissur'), ('Palakkad', 'Palakkad'), ('Malappuram', 'Malappuram'), ('Kozhikode', 'Kozhikode'), ('Wayanad', 'Wayanad'), ('Kannur', 'Kannur'), ('Kasaragod', 'Kasaragod')], max_length=50)),
                ('taluk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kvs_app.taluk_choices')),
            ],
        ),
        migrations.CreateModel(
            name='Matrimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=25)),
                ('dob', models.DateField()),
                ('age', models.IntegerField(blank=True, null=True)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('height', models.IntegerField()),
                ('work_place', models.CharField(blank=True, max_length=25, null=True)),
                ('languages', models.CharField(blank=True, max_length=250, null=True)),
                ('hobbies', models.CharField(blank=True, max_length=250, null=True)),
                ('brother', models.IntegerField()),
                ('father_name', models.CharField(max_length=25)),
                ('father_occupation', models.CharField(max_length=25)),
                ('mother_name', models.CharField(max_length=25)),
                ('mother_occupation', models.CharField(max_length=25)),
                ('sister', models.IntegerField()),
                ('total_family_members', models.IntegerField()),
                ('marital_status', models.CharField(choices=[('Un Married', 'Un Married'), ('Second Marriage', 'Second Marriage'), ('Divorced', 'Divorced'), ('Widow', 'Widow')], max_length=25)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='pictures')),
                ('education_qualification', models.CharField(max_length=250)),
                ('occupation', models.CharField(max_length=250)),
                ('district', models.CharField(choices=[('Trivandrum', 'Trivandrum'), ('Kollam', 'Kollam'), ('Pathanamthitta', 'Pathanamthitta'), ('Alappuzha', 'Alappuzha'), ('Kottayam', 'Kottayam'), ('Idukki', 'Idukki'), ('Ernakulam', 'Ernakulam'), ('Thrissur', 'Thrissur'), ('Palakkad', 'Palakkad'), ('Malappuram', 'Malappuram'), ('Kozhikode', 'Kozhikode'), ('Wayanad', 'Wayanad'), ('Kannur', 'Kannur'), ('Kasaragod', 'Kasaragod')], max_length=250)),
                ('taluk', models.CharField(max_length=50)),
                ('gaurdian_name', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Approved', max_length=25)),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kvs_app.gender_choices')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kvs_app.star')),
                ('subcaste', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kvs_app.subcaste_choices')),
            ],
        ),
        migrations.CreateModel(
            name='Join_Kvs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('mobile', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('place', models.CharField(max_length=25)),
                ('district', models.CharField(blank=True, choices=[('Trivandrum', 'Trivandrum'), ('Kollam', 'Kollam'), ('Pathanamthitta', 'Pathanamthitta'), ('Alappuzha', 'Alappuzha'), ('Kottayam', 'Kottayam'), ('Idukki', 'Idukki'), ('Ernakulam', 'Ernakulam'), ('Thrissur', 'Thrissur'), ('Palakkad', 'Palakkad'), ('Malappuram', 'Malappuram'), ('Kozhikode', 'Kozhikode'), ('Wayanad', 'Wayanad'), ('Kannur', 'Kannur'), ('Kasaragod', 'Kasaragod')], max_length=50, null=True)),
                ('sakha_no', models.CharField(blank=True, max_length=25, null=True)),
                ('id_proof_no', models.CharField(blank=True, max_length=25, null=True)),
                ('membership_no', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=25)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_proof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kvs_app.id_details_choices')),
                ('payment_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kvs_app.payment_details_choices')),
                ('sex', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kvs_app.sex_choices')),
                ('union', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kvs_app.taluk_choices')),
            ],
            options={
                'verbose_name_plural': 'Join Kvs',
            },
        ),
        migrations.CreateModel(
            name='ExtendedUserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Extended User Model',
            },
        ),
        migrations.CreateModel(
            name='Databank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=10)),
                ('occupation', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('taluk', models.CharField(max_length=50)),
                ('workplace', models.CharField(max_length=50)),
                ('contact_person', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('Hide', 'Hide'), ('Unhide', 'Unhide')], default='Unhide', max_length=25)),
                ('category', models.ForeignKey(blank=True, max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to='kvs_app.databankcategory')),
            ],
        ),
    ]
