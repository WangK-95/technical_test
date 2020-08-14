from django.conf.urls import url

from region.views import transfer_province, transfer_city, transfer_area, transfer_street

urlpatterns = [
    url(r'^transfer_province/', transfer_province),
    url(r'^transfer_city/', transfer_city),
    url(r'^transfer_area/', transfer_area),
    url(r'^transfer_street/', transfer_street),
]