# Generated by Django 2.1.2 on 2018-11-26 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opperation', '0002_txnba1718cgqb_txnba1718jhcj_txnba1718jhqb_txnba1718jqcj_txnba1718jqqb'),
    ]

    operations = [
        migrations.CreateModel(
            name='TxNba1516CgCj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paiming', models.CharField(blank=True, max_length=255, null=True)),
                ('qiuyuan', models.CharField(blank=True, max_length=255, null=True)),
                ('qiudui', models.CharField(blank=True, max_length=255, null=True)),
                ('defen_selected', models.CharField(blank=True, max_length=255, null=True)),
                ('chushou', models.CharField(blank=True, max_length=255, null=True)),
                ('mingzhong', models.CharField(blank=True, max_length=255, null=True)),
                ('chushou3', models.CharField(blank=True, max_length=255, null=True)),
                ('mingzhong3', models.CharField(blank=True, max_length=255, null=True)),
                ('faci', models.CharField(blank=True, max_length=255, null=True)),
                ('falv', models.CharField(blank=True, max_length=255, null=True)),
                ('lanban', models.CharField(blank=True, max_length=255, null=True)),
                ('qlanban', models.CharField(blank=True, max_length=255, null=True)),
                ('hlanban', models.CharField(blank=True, max_length=255, null=True)),
                ('zhugong', models.CharField(blank=True, max_length=255, null=True)),
                ('qiangduan', models.CharField(blank=True, max_length=255, null=True)),
                ('gaimao', models.CharField(blank=True, max_length=255, null=True)),
                ('shiwu', models.CharField(blank=True, max_length=255, null=True)),
                ('fangui', models.CharField(blank=True, max_length=255, null=True)),
                ('changci', models.CharField(blank=True, max_length=255, null=True)),
                ('shangchang', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'Tx_nba_1516_cg_cj',
            },
        ),
        migrations.CreateModel(
            name='TxNba1516CgQb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paiming', models.CharField(blank=True, max_length=255, null=True)),
                ('qiuyuan', models.CharField(blank=True, max_length=255, null=True)),
                ('qiudui', models.CharField(blank=True, max_length=255, null=True)),
                ('defen_selected', models.CharField(blank=True, max_length=255, null=True)),
                ('chushou', models.CharField(blank=True, max_length=255, null=True)),
                ('mingzhong', models.CharField(blank=True, max_length=255, null=True)),
                ('chushou3', models.CharField(blank=True, max_length=255, null=True)),
                ('mingzhong3', models.CharField(blank=True, max_length=255, null=True)),
                ('faci', models.CharField(blank=True, max_length=255, null=True)),
                ('falv', models.CharField(blank=True, max_length=255, null=True)),
                ('lanban', models.CharField(blank=True, max_length=255, null=True)),
                ('qlanban', models.CharField(blank=True, max_length=255, null=True)),
                ('hlanban', models.CharField(blank=True, max_length=255, null=True)),
                ('zhugong', models.CharField(blank=True, max_length=255, null=True)),
                ('qiangduan', models.CharField(blank=True, max_length=255, null=True)),
                ('gaimao', models.CharField(blank=True, max_length=255, null=True)),
                ('shiwu', models.CharField(blank=True, max_length=255, null=True)),
                ('fangui', models.CharField(blank=True, max_length=255, null=True)),
                ('changci', models.CharField(blank=True, max_length=255, null=True)),
                ('shangchang', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'Tx_nba_1516_cg_qb',
            },
        ),
        migrations.CreateModel(
            name='TxNba1516JhCj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paiming', models.CharField(blank=True, max_length=255, null=True)),
                ('qiuyuan', models.CharField(blank=True, max_length=255, null=True)),
                ('qiudui', models.CharField(blank=True, max_length=255, null=True)),
                ('defen_selected', models.CharField(blank=True, max_length=255, null=True)),
                ('chushou', models.CharField(blank=True, max_length=255, null=True)),
                ('mingzhong', models.CharField(blank=True, max_length=255, null=True)),
                ('chushou3', models.CharField(blank=True, max_length=255, null=True)),
                ('mingzhong3', models.CharField(blank=True, max_length=255, null=True)),
                ('faci', models.CharField(blank=True, max_length=255, null=True)),
                ('falv', models.CharField(blank=True, max_length=255, null=True)),
                ('lanban', models.CharField(blank=True, max_length=255, null=True)),
                ('qlanban', models.CharField(blank=True, max_length=255, null=True)),
                ('hlanban', models.CharField(blank=True, max_length=255, null=True)),
                ('zhugong', models.CharField(blank=True, max_length=255, null=True)),
                ('qiangduan', models.CharField(blank=True, max_length=255, null=True)),
                ('gaimao', models.CharField(blank=True, max_length=255, null=True)),
                ('shiwu', models.CharField(blank=True, max_length=255, null=True)),
                ('fangui', models.CharField(blank=True, max_length=255, null=True)),
                ('changci', models.CharField(blank=True, max_length=255, null=True)),
                ('shangchang', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'Tx_nba_1516_jh_cj',
            },
        ),
        migrations.CreateModel(
            name='TxNba1516JhQb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paiming', models.CharField(blank=True, max_length=255, null=True)),
                ('qiuyuan', models.CharField(blank=True, max_length=255, null=True)),
                ('qiudui', models.CharField(blank=True, max_length=255, null=True)),
                ('defen_selected', models.CharField(blank=True, max_length=255, null=True)),
                ('chushou', models.CharField(blank=True, max_length=255, null=True)),
                ('mingzhong', models.CharField(blank=True, max_length=255, null=True)),
                ('chushou3', models.CharField(blank=True, max_length=255, null=True)),
                ('mingzhong3', models.CharField(blank=True, max_length=255, null=True)),
                ('faci', models.CharField(blank=True, max_length=255, null=True)),
                ('falv', models.CharField(blank=True, max_length=255, null=True)),
                ('lanban', models.CharField(blank=True, max_length=255, null=True)),
                ('qlanban', models.CharField(blank=True, max_length=255, null=True)),
                ('hlanban', models.CharField(blank=True, max_length=255, null=True)),
                ('zhugong', models.CharField(blank=True, max_length=255, null=True)),
                ('qiangduan', models.CharField(blank=True, max_length=255, null=True)),
                ('gaimao', models.CharField(blank=True, max_length=255, null=True)),
                ('shiwu', models.CharField(blank=True, max_length=255, null=True)),
                ('fangui', models.CharField(blank=True, max_length=255, null=True)),
                ('changci', models.CharField(blank=True, max_length=255, null=True)),
                ('shangchang', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'Tx_nba_1516_jh_qb',
            },
        ),
        migrations.CreateModel(
            name='TxNba1516JqCj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paiming', models.CharField(blank=True, max_length=255, null=True)),
                ('qiuyuan', models.CharField(blank=True, max_length=255, null=True)),
                ('qiudui', models.CharField(blank=True, max_length=255, null=True)),
                ('defen_selected', models.CharField(blank=True, max_length=255, null=True)),
                ('chushou', models.CharField(blank=True, max_length=255, null=True)),
                ('mingzhong', models.CharField(blank=True, max_length=255, null=True)),
                ('chushou3', models.CharField(blank=True, max_length=255, null=True)),
                ('mingzhong3', models.CharField(blank=True, max_length=255, null=True)),
                ('faci', models.CharField(blank=True, max_length=255, null=True)),
                ('falv', models.CharField(blank=True, max_length=255, null=True)),
                ('lanban', models.CharField(blank=True, max_length=255, null=True)),
                ('qlanban', models.CharField(blank=True, max_length=255, null=True)),
                ('hlanban', models.CharField(blank=True, max_length=255, null=True)),
                ('zhugong', models.CharField(blank=True, max_length=255, null=True)),
                ('qiangduan', models.CharField(blank=True, max_length=255, null=True)),
                ('gaimao', models.CharField(blank=True, max_length=255, null=True)),
                ('shiwu', models.CharField(blank=True, max_length=255, null=True)),
                ('fangui', models.CharField(blank=True, max_length=255, null=True)),
                ('changci', models.CharField(blank=True, max_length=255, null=True)),
                ('shangchang', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'Tx_nba_1516_jq_cj',
            },
        ),
        migrations.CreateModel(
            name='TxNba1516JqQb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paiming', models.CharField(blank=True, max_length=255, null=True)),
                ('qiuyuan', models.CharField(blank=True, max_length=255, null=True)),
                ('qiudui', models.CharField(blank=True, max_length=255, null=True)),
                ('defen_selected', models.CharField(blank=True, max_length=255, null=True)),
                ('chushou', models.CharField(blank=True, max_length=255, null=True)),
                ('mingzhong', models.CharField(blank=True, max_length=255, null=True)),
                ('chushou3', models.CharField(blank=True, max_length=255, null=True)),
                ('mingzhong3', models.CharField(blank=True, max_length=255, null=True)),
                ('faci', models.CharField(blank=True, max_length=255, null=True)),
                ('falv', models.CharField(blank=True, max_length=255, null=True)),
                ('lanban', models.CharField(blank=True, max_length=255, null=True)),
                ('qlanban', models.CharField(blank=True, max_length=255, null=True)),
                ('hlanban', models.CharField(blank=True, max_length=255, null=True)),
                ('zhugong', models.CharField(blank=True, max_length=255, null=True)),
                ('qiangduan', models.CharField(blank=True, max_length=255, null=True)),
                ('gaimao', models.CharField(blank=True, max_length=255, null=True)),
                ('shiwu', models.CharField(blank=True, max_length=255, null=True)),
                ('fangui', models.CharField(blank=True, max_length=255, null=True)),
                ('changci', models.CharField(blank=True, max_length=255, null=True)),
                ('shangchang', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'Tx_nba_1516_jq_qb',
            },
        ),
        migrations.CreateModel(
            name='TxNba1617CgCj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paiming', models.CharField(blank=True, max_length=255, null=True)),
                ('qiuyuan', models.CharField(blank=True, max_length=255, null=True)),
                ('qiudui', models.CharField(blank=True, max_length=255, null=True)),
                ('defen_selected', models.CharField(blank=True, max_length=255, null=True)),
                ('chushou', models.CharField(blank=True, max_length=255, null=True)),
                ('mingzhong', models.CharField(blank=True, max_length=255, null=True)),
                ('chushou3', models.CharField(blank=True, max_length=255, null=True)),
                ('mingzhong3', models.CharField(blank=True, max_length=255, null=True)),
                ('faci', models.CharField(blank=True, max_length=255, null=True)),
                ('falv', models.CharField(blank=True, max_length=255, null=True)),
                ('lanban', models.CharField(blank=True, max_length=255, null=True)),
                ('qlanban', models.CharField(blank=True, max_length=255, null=True)),
                ('hlanban', models.CharField(blank=True, max_length=255, null=True)),
                ('zhugong', models.CharField(blank=True, max_length=255, null=True)),
                ('qiangduan', models.CharField(blank=True, max_length=255, null=True)),
                ('gaimao', models.CharField(blank=True, max_length=255, null=True)),
                ('shiwu', models.CharField(blank=True, max_length=255, null=True)),
                ('fangui', models.CharField(blank=True, max_length=255, null=True)),
                ('changci', models.CharField(blank=True, max_length=255, null=True)),
                ('shangchang', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'Tx_nba_1617_cg_cj',
            },
        ),
        migrations.CreateModel(
            name='TxNba1617CgQb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paiming', models.CharField(blank=True, max_length=255, null=True)),
                ('qiuyuan', models.CharField(blank=True, max_length=255, null=True)),
                ('qiudui', models.CharField(blank=True, max_length=255, null=True)),
                ('defen_selected', models.CharField(blank=True, max_length=255, null=True)),
                ('chushou', models.CharField(blank=True, max_length=255, null=True)),
                ('mingzhong', models.CharField(blank=True, max_length=255, null=True)),
                ('chushou3', models.CharField(blank=True, max_length=255, null=True)),
                ('mingzhong3', models.CharField(blank=True, max_length=255, null=True)),
                ('faci', models.CharField(blank=True, max_length=255, null=True)),
                ('falv', models.CharField(blank=True, max_length=255, null=True)),
                ('lanban', models.CharField(blank=True, max_length=255, null=True)),
                ('qlanban', models.CharField(blank=True, max_length=255, null=True)),
                ('hlanban', models.CharField(blank=True, max_length=255, null=True)),
                ('zhugong', models.CharField(blank=True, max_length=255, null=True)),
                ('qiangduan', models.CharField(blank=True, max_length=255, null=True)),
                ('gaimao', models.CharField(blank=True, max_length=255, null=True)),
                ('shiwu', models.CharField(blank=True, max_length=255, null=True)),
                ('fangui', models.CharField(blank=True, max_length=255, null=True)),
                ('changci', models.CharField(blank=True, max_length=255, null=True)),
                ('shangchang', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'Tx_nba_1617_cg_qb',
            },
        ),
        migrations.CreateModel(
            name='TxNba1617JhCj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paiming', models.CharField(blank=True, max_length=255, null=True)),
                ('qiuyuan', models.CharField(blank=True, max_length=255, null=True)),
                ('qiudui', models.CharField(blank=True, max_length=255, null=True)),
                ('defen_selected', models.CharField(blank=True, max_length=255, null=True)),
                ('chushou', models.CharField(blank=True, max_length=255, null=True)),
                ('mingzhong', models.CharField(blank=True, max_length=255, null=True)),
                ('chushou3', models.CharField(blank=True, max_length=255, null=True)),
                ('mingzhong3', models.CharField(blank=True, max_length=255, null=True)),
                ('faci', models.CharField(blank=True, max_length=255, null=True)),
                ('falv', models.CharField(blank=True, max_length=255, null=True)),
                ('lanban', models.CharField(blank=True, max_length=255, null=True)),
                ('qlanban', models.CharField(blank=True, max_length=255, null=True)),
                ('hlanban', models.CharField(blank=True, max_length=255, null=True)),
                ('zhugong', models.CharField(blank=True, max_length=255, null=True)),
                ('qiangduan', models.CharField(blank=True, max_length=255, null=True)),
                ('gaimao', models.CharField(blank=True, max_length=255, null=True)),
                ('shiwu', models.CharField(blank=True, max_length=255, null=True)),
                ('fangui', models.CharField(blank=True, max_length=255, null=True)),
                ('changci', models.CharField(blank=True, max_length=255, null=True)),
                ('shangchang', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'Tx_nba_1617_jh_cj',
            },
        ),
        migrations.CreateModel(
            name='TxNba1617JhQb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paiming', models.CharField(blank=True, max_length=255, null=True)),
                ('qiuyuan', models.CharField(blank=True, max_length=255, null=True)),
                ('qiudui', models.CharField(blank=True, max_length=255, null=True)),
                ('defen_selected', models.CharField(blank=True, max_length=255, null=True)),
                ('chushou', models.CharField(blank=True, max_length=255, null=True)),
                ('mingzhong', models.CharField(blank=True, max_length=255, null=True)),
                ('chushou3', models.CharField(blank=True, max_length=255, null=True)),
                ('mingzhong3', models.CharField(blank=True, max_length=255, null=True)),
                ('faci', models.CharField(blank=True, max_length=255, null=True)),
                ('falv', models.CharField(blank=True, max_length=255, null=True)),
                ('lanban', models.CharField(blank=True, max_length=255, null=True)),
                ('qlanban', models.CharField(blank=True, max_length=255, null=True)),
                ('hlanban', models.CharField(blank=True, max_length=255, null=True)),
                ('zhugong', models.CharField(blank=True, max_length=255, null=True)),
                ('qiangduan', models.CharField(blank=True, max_length=255, null=True)),
                ('gaimao', models.CharField(blank=True, max_length=255, null=True)),
                ('shiwu', models.CharField(blank=True, max_length=255, null=True)),
                ('fangui', models.CharField(blank=True, max_length=255, null=True)),
                ('changci', models.CharField(blank=True, max_length=255, null=True)),
                ('shangchang', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'Tx_nba_1617_jh_qb',
            },
        ),
        migrations.CreateModel(
            name='TxNba1617JqCj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paiming', models.CharField(blank=True, max_length=255, null=True)),
                ('qiuyuan', models.CharField(blank=True, max_length=255, null=True)),
                ('qiudui', models.CharField(blank=True, max_length=255, null=True)),
                ('defen_selected', models.CharField(blank=True, max_length=255, null=True)),
                ('chushou', models.CharField(blank=True, max_length=255, null=True)),
                ('mingzhong', models.CharField(blank=True, max_length=255, null=True)),
                ('chushou3', models.CharField(blank=True, max_length=255, null=True)),
                ('mingzhong3', models.CharField(blank=True, max_length=255, null=True)),
                ('faci', models.CharField(blank=True, max_length=255, null=True)),
                ('falv', models.CharField(blank=True, max_length=255, null=True)),
                ('lanban', models.CharField(blank=True, max_length=255, null=True)),
                ('qlanban', models.CharField(blank=True, max_length=255, null=True)),
                ('hlanban', models.CharField(blank=True, max_length=255, null=True)),
                ('zhugong', models.CharField(blank=True, max_length=255, null=True)),
                ('qiangduan', models.CharField(blank=True, max_length=255, null=True)),
                ('gaimao', models.CharField(blank=True, max_length=255, null=True)),
                ('shiwu', models.CharField(blank=True, max_length=255, null=True)),
                ('fangui', models.CharField(blank=True, max_length=255, null=True)),
                ('changci', models.CharField(blank=True, max_length=255, null=True)),
                ('shangchang', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'Tx_nba_1617_jq_cj',
            },
        ),
        migrations.CreateModel(
            name='TxNba1617JqQb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paiming', models.CharField(blank=True, max_length=255, null=True)),
                ('qiuyuan', models.CharField(blank=True, max_length=255, null=True)),
                ('qiudui', models.CharField(blank=True, max_length=255, null=True)),
                ('defen_selected', models.CharField(blank=True, max_length=255, null=True)),
                ('chushou', models.CharField(blank=True, max_length=255, null=True)),
                ('mingzhong', models.CharField(blank=True, max_length=255, null=True)),
                ('chushou3', models.CharField(blank=True, max_length=255, null=True)),
                ('mingzhong3', models.CharField(blank=True, max_length=255, null=True)),
                ('faci', models.CharField(blank=True, max_length=255, null=True)),
                ('falv', models.CharField(blank=True, max_length=255, null=True)),
                ('lanban', models.CharField(blank=True, max_length=255, null=True)),
                ('qlanban', models.CharField(blank=True, max_length=255, null=True)),
                ('hlanban', models.CharField(blank=True, max_length=255, null=True)),
                ('zhugong', models.CharField(blank=True, max_length=255, null=True)),
                ('qiangduan', models.CharField(blank=True, max_length=255, null=True)),
                ('gaimao', models.CharField(blank=True, max_length=255, null=True)),
                ('shiwu', models.CharField(blank=True, max_length=255, null=True)),
                ('fangui', models.CharField(blank=True, max_length=255, null=True)),
                ('changci', models.CharField(blank=True, max_length=255, null=True)),
                ('shangchang', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'Tx_nba_1617_jq_qb',
            },
        ),
    ]
