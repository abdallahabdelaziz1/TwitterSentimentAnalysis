# Generated by Django 3.2.9 on 2021-12-01 05:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoAPI', '0003_auto_20211201_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='Suggested_Sentiment',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='hour',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(23), django.core.validators.MinValueValidator(0)]),
        ),
    ]
