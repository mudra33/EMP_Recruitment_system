# Generated by Django 3.0.4 on 2020-05-06 13:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0017_auto_20200506_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_details',
            name='jd_apply_by',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='job_details',
            name='jd_start_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]