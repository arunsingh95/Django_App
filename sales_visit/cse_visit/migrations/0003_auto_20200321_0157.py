# Generated by Django 2.2 on 2020-03-20 20:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cse_visit', '0002_auto_20200320_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customervisitdetails',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='documents/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
    ]
