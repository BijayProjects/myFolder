# Generated by Django 5.0 on 2024-11-17 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_product', '0003_sv_img_img_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sv_img',
            name='img_name',
            field=models.ImageField(upload_to='Media'),
        ),
    ]
