from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Region(MPTTModel):
    name = models.CharField(max_length=50, verbose_name=_('名称'))
    short_name = models.CharField(max_length=50, verbose_name=_('简称'))
    code = models.CharField(max_length=40, null=True, verbose_name=_('编号'))
    lng = models.CharField(max_length=20, verbose_name=_('经度'))
    lat = models.CharField(max_length=20, verbose_name=_('纬度'))
    parent = TreeForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children', db_index=True, verbose_name=_('父级'))

    class Meta:
        app_label = "region"
        db_table = 'region'
        verbose_name = _('地区')


class Province(models.Model):
    code = models.CharField(max_length=40, verbose_name=_('编号'))
    name = models.CharField(max_length=30, verbose_name=_('名称'))
    short_name = models.CharField(max_length=10, verbose_name=_('简称'))
    lng = models.CharField(max_length=20, verbose_name=_('经度'))
    lat = models.CharField(max_length=20, verbose_name=_('纬度'))

    class Meta:
        app_label = "region"
        db_table = 'region_province'
        verbose_name = _('省份')


class City(models.Model):
    code = models.CharField(max_length=40, verbose_name=_('编号'))
    name = models.CharField(max_length=30, verbose_name=_('名称'))
    short_name = models.CharField(max_length=10, verbose_name=_('简称'))
    lng = models.CharField(max_length=20, verbose_name=_('经度'))
    lat = models.CharField(max_length=20, verbose_name=_('纬度'))
    province_code = models.CharField(max_length=40, verbose_name=_('省份编号'))

    class Meta:
        app_label = "region"
        db_table = 'region_city'
        verbose_name = _('城市')


class Area(models.Model):
    code = models.CharField(max_length=40, verbose_name=_('编号'))
    name = models.CharField(max_length=50, verbose_name=_('名称'))
    short_name = models.CharField(max_length=50, verbose_name=_('简称'))
    lng = models.CharField(max_length=20, verbose_name=_('经度'))
    lat = models.CharField(max_length=20, verbose_name=_('纬度'))
    city_code = models.CharField(max_length=40, verbose_name=_('城市编号'))

    class Meta:
        app_label = "region"
        db_table = 'region_area'
        verbose_name = _('区域')


class Street(models.Model):
    code = models.CharField(max_length=40, verbose_name=_('编号'))
    name = models.CharField(max_length=50, verbose_name=_('名称'))
    short_name = models.CharField(max_length=50, verbose_name=_('简称'))
    lng = models.CharField(max_length=20, verbose_name=_('经度'))
    lat = models.CharField(max_length=20, verbose_name=_('纬度'))
    area_code = models.CharField(max_length=40, verbose_name=_('区域编号'))

    class Meta:
        app_label = "region"
        db_table = 'region_street'
        verbose_name = _('街道')
