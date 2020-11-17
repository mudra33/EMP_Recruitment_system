# Generated by Django 3.0.4 on 2020-03-30 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='job_seeker',
            fields=[
                ('f_name', models.CharField(max_length=50)),
                ('m_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
                ('uid_type', models.CharField(max_length=50)),
                ('uid_number', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('dob', models.DateField()),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=20)),
                ('add', models.CharField(max_length=70)),
                ('pincode', models.CharField(max_length=10)),
                ('email_id', models.EmailField(max_length=254)),
                ('mobile_no', models.CharField(max_length=11)),
                ('pwd', models.CharField(max_length=11)),
                ('u_name', models.CharField(max_length=50)),
            ],
        ),
    ]