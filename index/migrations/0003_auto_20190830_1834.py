# Generated by Django 2.1.8 on 2019-08-30 10:34

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_home_infor_hotel_datail_hotel_infor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attractions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40, verbose_name='景点名称')),
                ('address', models.CharField(max_length=100, verbose_name='详细地址')),
                ('datail', ckeditor.fields.RichTextField(verbose_name='详情信息')),
                ('sugget', models.FloatField(verbose_name='是否推荐,1为推荐')),
                ('city', models.CharField(max_length=40, verbose_name='所在省')),
                ('area', models.CharField(max_length=40, verbose_name='所在市')),
                ('summary', models.CharField(max_length=100, verbose_name='概要')),
                ('type', models.CharField(max_length=50, verbose_name='景点类型')),
            ],
            options={
                'verbose_name': '景点信息',
                'db_table': 'Attractions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Attractions_price',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40, verbose_name='景点名称')),
                ('child_price', models.FloatField(verbose_name='儿童票价')),
                ('stu_price', models.FloatField(verbose_name='学生票价')),
                ('adult_price', models.FloatField(verbose_name='成人票价')),
            ],
            options={
                'verbose_name': '景点门票价格',
                'db_table': 'Attractions_price',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Banner_img',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('img', models.ImageField(upload_to='banner/', verbose_name='轮播图')),
                ('href', models.CharField(max_length=80, verbose_name='广告链接')),
            ],
            options={
                'verbose_name': '轮播图',
                'db_table': 'Bannber_img',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Flow',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40, verbose_name='景点名称')),
                ('max', models.FloatField(verbose_name='最大客流量')),
                ('time1_flow', models.FloatField(verbose_name='第一个月的客流量')),
                ('time2_flow', models.FloatField(verbose_name='第二个月的客流量')),
                ('time3_flow', models.FloatField(verbose_name='第三个月的客流量')),
                ('time4_flow', models.FloatField(verbose_name='第四个月的客流量')),
                ('time5_flow', models.FloatField(verbose_name='第五个月的客流量')),
                ('time6_flow', models.FloatField(verbose_name='第六个月的客流量')),
                ('flow_img', models.CharField(max_length=2083, verbose_name='流量折线图')),
            ],
            options={
                'verbose_name': '景点流量信息',
                'db_table': 'Flow',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='新闻标题')),
                ('summary', models.CharField(max_length=100, verbose_name='新闻概要')),
                ('datail', ckeditor.fields.RichTextField(verbose_name='新闻详情')),
                ('auth_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='新闻发布时间')),
                ('news_img', models.ImageField(upload_to='news/%y/%m/%d')),
            ],
            options={
                'verbose_name': '新闻',
                'db_table': 'News',
                'managed': False,
            },
        ),
        migrations.AlterModelTable(
            name='home_infor',
            table='Home_infor',
        ),
        migrations.AlterModelTable(
            name='hotel_datail',
            table='Hotel_detail',
        ),
        migrations.AlterModelTable(
            name='hotel_infor',
            table='Hotel_infor',
        ),
        migrations.AlterModelTable(
            name='order',
            table='Order',
        ),
    ]
