# Generated by Django 3.0.4 on 2020-05-06 14:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0019_auto_20200506_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_details',
            name='jd_apply_by',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='job_details',
            name='jd_start_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]