# Generated by Django 2.1.2 on 2018-12-24 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ttq', models.CharField(max_length=100, verbose_name='测试')),
            ],
            options={
                'verbose_name': 'tt',
                'verbose_name_plural': 'tt',
            },
        ),
    ]