# Generated by Django 3.0.6 on 2020-05-28 10:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20200527_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.CharField(blank=True, max_length=60, validators=[django.core.validators.RegexValidator('^[, a-zA-Z]*$', 'Enter comma separated tags. (use space for two words tag)')]),
        ),
    ]
