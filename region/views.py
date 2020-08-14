from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from region.models import Province, Region, City, Area, Street


@transaction.atomic
def transfer_province(self):
    province_all = Province.objects.all()
    for item in province_all:
        Region.objects.create(name=item.name, code=item.code, short_name=item.short_name, lng=item.lng, lat=item.lat)
    return HttpResponse('this is response test!')


@transaction.atomic
def transfer_city(self):
    city_all = City.objects.all()
    region_list = Region.objects.filter(level=0).values('id', 'code')
    region_dict = {}
    for item in region_list:
        region_dict[item['code']] = item['id']
    for item in city_all:
        Region.objects.create(name=item.name, code=item.code, short_name=item.short_name, lng=item.lng, lat=item.lat, parent_id=region_dict[item.province_code])
    return HttpResponse('this is response test!')


@transaction.atomic
def transfer_area(self):
    area_all = Area.objects.all()
    region_list = Region.objects.filter(level=1).values('id', 'code')
    region_dict = {}
    for item in region_list:
        region_dict[item['code']] = item['id']
    for item in area_all:
        Region.objects.create(name=item.name, code=item.code, short_name=item.short_name, lng=item.lng, lat=item.lat, parent_id=region_dict[item.city_code])
    return HttpResponse('this is response test!')


@transaction.atomic
def transfer_street(self):
    street_all = Street.objects.all()
    region_list = Region.objects.filter(level=2).values('id', 'code')
    region_dict = {}
    for item in region_list:
        region_dict[item['code']] = item['id']
    for item in street_all:
        Region.objects.create(name=item.name, code=item.code, short_name=item.short_name, lng=item.lng, lat=item.lat, parent_id=region_dict[item.area_code])
    return HttpResponse('this is response test!')
