# Generated by Django 2.1.2 on 2018-11-28 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opperation', '0003_txnba1516cgcj_txnba1516cgqb_txnba1516jhcj_txnba1516jhqb_txnba1516jqcj_txnba1516jqqb_txnba1617cgcj_tx'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerInfo',
            fields=[
                ('team_img', models.CharField(blank=True, max_length=255, null=True)),
                ('start_urls', models.CharField(blank=True, max_length=255, null=True)),
                ('imgurl', models.CharField(blank=True, max_length=255, null=True)),
                ('c_name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('e_name', models.CharField(max_length=255)),
                ('player_number', models.CharField(blank=True, max_length=255, null=True)),
                ('weizhi', models.CharField(blank=True, max_length=255, null=True)),
                ('shengao', models.CharField(blank=True, max_length=255, null=True)),
                ('tizhong', models.CharField(blank=True, max_length=255, null=True)),
                ('shengri', models.CharField(blank=True, max_length=255, null=True)),
                ('hetong', models.CharField(blank=True, max_length=255, null=True)),
                ('hetong2', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'player_info',
                'managed': False,
            },
        ),
    ]
