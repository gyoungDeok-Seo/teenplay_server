# Generated by Django 5.0.2 on 2024-03-14 10:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0003_alter_activity_activity_address_detail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityimage',
            name='activity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='activity.activity'),
        ),
    ]
