# Generated by Django 2.1.2 on 2018-12-24 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20181224_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meseagesetting',
            name='is_read',
            field=models.IntegerField(verbose_name='是否已经阅读'),
        ),
    ]
