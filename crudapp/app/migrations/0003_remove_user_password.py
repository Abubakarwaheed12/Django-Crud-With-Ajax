# Generated by Django 3.2.12 on 2023-01-09 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20230109_0727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
    ]
