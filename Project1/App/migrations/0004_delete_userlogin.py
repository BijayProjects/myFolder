# Generated by Django 5.1.3 on 2024-11-14 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_rename_user_userlogin'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserLogin',
        ),
    ]
