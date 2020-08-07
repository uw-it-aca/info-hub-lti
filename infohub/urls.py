from django.urls import re_path
from infohub.views import InfoHubView

urlpatterns = [
    re_path(r'^$', InfoHubView.as_view()),
]
