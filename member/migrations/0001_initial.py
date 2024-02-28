# Generated by Django 5.0.2 on 2024-02-28 19:27

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('member_email', models.TextField()),
                ('member_nickname', models.TextField()),
                ('member_phone', models.TextField()),
                ('member_address', models.TextField()),
                ('member_gender', models.SmallIntegerField(choices=[(0, '선택안함'), (1, '남성'), (2, '여성')], default=0)),
                ('member_marketing_agree', models.BooleanField(default=0)),
                ('member_privacy_agree', models.BooleanField(default=0)),
                ('status', models.SmallIntegerField(choices=[(-1, '정지'), (0, '탈퇴'), (1, '활동중')], default=1)),
                ('profile_path', models.ImageField(upload_to='member/%Y/%m/%d')),
            ],
            options={
                'db_table': 'tbl_member',
            },
        ),
    ]
