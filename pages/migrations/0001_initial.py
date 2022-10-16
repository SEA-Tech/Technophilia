# Generated by Django 3.0.5 on 2022-10-16 13:05

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodBank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('contact', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=255)),
                ('pincode', models.PositiveIntegerField()),
                ('city', models.CharField(default='', max_length=125)),
                ('country', models.CharField(max_length=125)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('contact', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=255)),
                ('pincode', models.PositiveIntegerField()),
                ('city', models.CharField(default='', max_length=125)),
                ('country', models.CharField(max_length=125)),
                ('op', models.IntegerField(default=0)),
                ('on', models.IntegerField(default=0)),
                ('ap', models.IntegerField(default=0)),
                ('an', models.IntegerField(default=0)),
                ('bp', models.IntegerField(default=0)),
                ('bn', models.IntegerField(default=0)),
                ('abp', models.IntegerField(default=0)),
                ('abn', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='HospitalUse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group', models.CharField(max_length=50)),
                ('time_of_use', models.DateTimeField(auto_now_add=True)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Hospital')),
            ],
        ),
        migrations.CreateModel(
            name='HospitalDonation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_of_donation', models.DateTimeField(auto_now_add=True)),
                ('donor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('hospital', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('aadhar_no', models.CharField(max_length=15)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(70)])),
                ('address', models.CharField(max_length=255)),
                ('blood_group', models.TextField(choices=[('A RhD positive (A+)', 'A RhD positive (A+)'), ('A RhD negative (A-)', 'A RhD negative (A-)'), ('B RhD positive (B+)', 'B RhD positive (B+)'), ('B RhD negative (B-)', 'B RhD negative (B-)'), ('O RhD positive (O+)', 'O RhD positive (O+)'), ('O RhD negative (O-)', 'O RhD negative (O-)'), ('AB RhD positive (AB+)', 'AB RhD positive (AB+)'), ('AB RhD negative (AB-)', 'AB RhD negative (AB-)')])),
                ('approved', models.BooleanField(default=False)),
                ('time_of_donation', models.DateTimeField(auto_now_add=True)),
                ('hospital', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Hospital')),
            ],
        ),
        migrations.CreateModel(
            name='DonationRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group', models.CharField(choices=[('A RhD positive (A+)', 'A RhD positive (A+)'), ('A RhD negative (A-)', 'A RhD negative (A-)'), ('B RhD positive (B+)', 'B RhD positive (B+)'), ('B RhD negative (B-)', 'B RhD negative (B-)'), ('O RhD positive (O+)', 'O RhD positive (O+)'), ('O RhD negative (O-)', 'O RhD negative (O-)'), ('AB RhD positive (AB+)', 'AB RhD positive (AB+)'), ('AB RhD negative (AB-)', 'AB RhD negative (AB-)')], max_length=50)),
                ('satisfied', models.BooleanField(default=False)),
                ('time_of_request', models.DateTimeField(auto_now_add=True)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Hospital')),
            ],
        ),
    ]