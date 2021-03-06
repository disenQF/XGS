# Generated by Django 2.1.5 on 2019-01-22 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='新增时间')),
                ('last_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=100, verbose_name='口令')),
                ('email', models.CharField(max_length=50, verbose_name='邮箱')),
                ('phone', models.CharField(max_length=11, verbose_name='手机')),
            ],
            options={
                'verbose_name': '客户信息',
                'verbose_name_plural': '客户信息',
                'db_table': 'app_user',
                'ordering': ['-last_time'],
            },
        ),
    ]
