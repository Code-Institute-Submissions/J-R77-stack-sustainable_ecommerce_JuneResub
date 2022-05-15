# Generated by Django 3.2 on 2022-05-15 08:34

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_userprofile_default_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_country',
            field=django_countries.fields.CountryField(default='GB', max_length=2),
        ),
    ]