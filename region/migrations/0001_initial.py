# Generated by Django 3.1 on 2020-08-12 06:54

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=40, verbose_name='编号')),
                ('name', models.CharField(max_length=30, verbose_name='名称')),
                ('short_name', models.CharField(max_length=10, verbose_name='简称')),
                ('lng', models.CharField(max_length=20, verbose_name='经度')),
                ('lat', models.CharField(max_length=20, verbose_name='纬度')),
                ('city_code', models.CharField(max_length=40, verbose_name='城市编号')),
            ],
            options={
                'verbose_name': '区域',
                'db_table': 'region_area',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=40, verbose_name='编号')),
                ('name', models.CharField(max_length=30, verbose_name='名称')),
                ('short_name', models.CharField(max_length=10, verbose_name='简称')),
                ('lng', models.CharField(max_length=20, verbose_name='经度')),
                ('lat', models.CharField(max_length=20, verbose_name='纬度')),
                ('province_code', models.CharField(max_length=40, verbose_name='省份编号')),
            ],
            options={
                'verbose_name': '城市',
                'db_table': 'region_city',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=40, verbose_name='编号')),
                ('name', models.CharField(max_length=30, verbose_name='名称')),
                ('short_name', models.CharField(max_length=10, verbose_name='简称')),
                ('lng', models.CharField(max_length=20, verbose_name='经度')),
                ('lat', models.CharField(max_length=20, verbose_name='纬度')),
            ],
            options={
                'verbose_name': '省份',
                'db_table': 'region_province',
            },
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=40, verbose_name='编号')),
                ('name', models.CharField(max_length=30, verbose_name='名称')),
                ('short_name', models.CharField(max_length=10, verbose_name='简称')),
                ('lng', models.CharField(max_length=20, verbose_name='经度')),
                ('lat', models.CharField(max_length=20, verbose_name='纬度')),
                ('area_code', models.CharField(max_length=40, verbose_name='区域编号')),
            ],
            options={
                'verbose_name': '街道',
                'db_table': 'region_street',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='名称')),
                ('short_name', models.CharField(max_length=10, verbose_name='简称')),
                ('lng', models.CharField(max_length=20, verbose_name='经度')),
                ('lat', models.CharField(max_length=20, verbose_name='纬度')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='region.region', verbose_name='父级')),
            ],
            options={
                'verbose_name': '地区',
                'db_table': 'region',
            },
        ),
    ]