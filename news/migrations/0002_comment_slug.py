# Generated by Django 3.1.7 on 2021-03-04 13:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=255, unique=True, verbose_name='Url'),
            preserve_default=False,
        ),
    ]
