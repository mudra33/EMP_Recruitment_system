# Generated by Django 3.0.4 on 2020-05-12 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0025_auto_20200512_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewapplicants',
            name='va_status',
            field=models.CharField(default='Pending', max_length=20),
        ),
    ]