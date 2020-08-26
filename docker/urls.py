from .base_urls import *
from django.conf.urls import include, re_path


urlpatterns += [
    re_path(r'^infohub', include('infohub.urls')),
]
