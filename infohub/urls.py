# Copyright 2024 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0


from django.urls import re_path
from infohub.views import InfoHubLaunchView, InfoHubView


urlpatterns = [
    re_path(r'^$', InfoHubLaunchView.as_view()),
    re_path(r'^hub[\/]?$',  InfoHubView.as_view(), name="infohub"),
]
