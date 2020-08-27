from django.conf import settings
from django.urls import re_path
from infohub.views import InfoHubView

urlpatterns = [
    re_path(r'^$', InfoHubView.as_view()),
]

if getattr(settings, "DEBUG", False):
    from infohub.views import InfoHubDevPrepare, InfoHubDevLaunch
    urlpatterns += [
        re_path(r'dev[/]?$', InfoHubDevPrepare.as_view()),
        re_path(r'dev/launch[/]?', InfoHubDevLaunch.as_view()),
    ]
