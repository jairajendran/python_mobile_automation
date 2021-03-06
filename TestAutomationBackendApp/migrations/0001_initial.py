# Generated by Django 3.0.5 on 2021-02-02 12:21

import TestAutomationBackendApp.models
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('appName', models.CharField(max_length=23)),
                ('totalDevices', models.BigIntegerField(verbose_name=10)),
                ('totalScenarios', models.BigIntegerField(verbose_name=10)),
                ('activeStatus', models.BooleanField(default=True)),
                ('preConditionStatus', models.BigIntegerField(verbose_name=10)),
                ('objectRunStatus', models.BigIntegerField(verbose_name=10)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceId', models.CharField(max_length=23)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(blank=True, max_length=128)),
                ('last_name', models.CharField(blank=True, max_length=128)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('ExecutionStatus', models.BooleanField(default=False)),
                ('requestUser', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ExecutionData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userEmail', models.EmailField(max_length=254)),
                ('devices', models.TextField()),
                ('applicationId', models.BigIntegerField(verbose_name=10)),
                ('executionStatus', models.IntegerField(verbose_name=10)),
                ('executionDate', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(blank=True, max_length=128)),
                ('last_name', models.CharField(blank=True, max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('roles', models.CharField(choices=[('User', 'User'), ('Admin', 'Admin')], max_length=20)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='TestScenarios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('scenarioName', models.CharField(max_length=50)),
                ('scenarioDescription', models.CharField(max_length=100)),
                ('activeStatus', models.BooleanField(default=True)),
                ('_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testscenarios', to='TestAutomationBackendApp.Application')),
            ],
        ),
        migrations.CreateModel(
            name='TestData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('testDataName', models.CharField(max_length=50)),
                ('testDataDescription', models.CharField(max_length=50)),
                ('testDataStatus', models.BooleanField(default=True)),
                ('_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testdata', to='TestAutomationBackendApp.TestScenarios')),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_class', models.CharField(max_length=100)),
                ('_id', models.CharField(max_length=23)),
                ('communicationPort', models.CharField(max_length=23)),
                ('deviceState', models.CharField(max_length=23)),
                ('deviceStatus', models.BooleanField(default=False)),
                ('emailId', models.CharField(max_length=60)),
                ('imagePort', models.CharField(max_length=23)),
                ('imei', models.CharField(max_length=23)),
                ('ipAddress', models.CharField(max_length=23)),
                ('location', djongo.models.fields.EmbeddedField(default=None, model_container=TestAutomationBackendApp.models.Location)),
                ('macAddress', models.CharField(max_length=23)),
                ('mdn', models.CharField(max_length=23)),
                ('modelName', models.CharField(max_length=23)),
                ('modelNumber', models.CharField(max_length=23)),
                ('oem', models.CharField(max_length=23)),
                ('oemColor', models.CharField(max_length=23)),
                ('os', models.CharField(max_length=23)),
                ('osVersion', models.CharField(max_length=23)),
                ('serialNumber', models.CharField(max_length=23)),
                ('team', models.CharField(max_length=23)),
                ('videoStreamingPort', models.CharField(max_length=23)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='TestAutomationBackendApp.DeviceUser')),
            ],
        ),
    ]
