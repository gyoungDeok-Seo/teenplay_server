# Generated by Django 5.0.2 on 2024-03-04 12:53

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('festival', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='festival',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]