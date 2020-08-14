from region.models import Province, Region


def merge_data():
    pass


def transfer_province():
    province_all = Province.objects.all()
    region_list = [Region(name=item.name, code=item.code, short_name=item.short_name, lng=item.lng, lat=item.lat) for item in province_all]
    Region.objects.bulk_create(region_list)


if __name__ == '__main__':
    transfer_province()
