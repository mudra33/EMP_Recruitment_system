# Generated by Django 3.0.4 on 2020-03-31 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0005_auto_20200331_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_provider',
            name='job_provider_company_id',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, primary_key=True, serialize=False, to='MyApp.company'),
        ),
    ]
