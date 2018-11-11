# Generated by Django 2.1.3 on 2018-11-10 23:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=20, unique=True, validators=[django.core.validators.RegexValidator('^[a-z0-9]+$', 'Problem code must be made of characters and/or numbers.')])),
                ('name', models.CharField(max_length=200, unique=True)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('executives', models.CharField(blank=True, help_text='The executives of the club.', max_length=400)),
                ('description', models.TextField(blank=True, help_text='A description of the club.')),
            ],
            options={
                'db_table': 'club',
            },
        ),
    ]
