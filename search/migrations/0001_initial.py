# Generated by Django 5.0.2 on 2024-02-28 19:29

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecentSearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('keyword', models.TextField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='member.member')),
            ],
            options={
                'db_table': 'tbl_recent_search',
            },
        ),
    ]