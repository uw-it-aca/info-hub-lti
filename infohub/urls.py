# Copyright 2025 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0


from django.urls import re_path
from infohub.views import InfoHubLaunchView


urlpatterns = [
    re_path(r'^$', InfoHubLaunchView.as_view(), name="lti-launch"),
]
