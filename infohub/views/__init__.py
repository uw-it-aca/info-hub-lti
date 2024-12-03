# Copyright 2024 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0


from django.conf import settings
from django.shortcuts import redirect
from blti import BLTIException
from blti.views import BLTILaunchView
from blti.validators import Roles
from uw_canvas.models import CanvasCourse
import re


class InfoHubLaunchView(BLTILaunchView):
    template_name = 'infohub/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        account_sis_id = self.blti.account_sis_id
        context['user_login_id'] = self.blti.user_login_id
        context['user_first_name'] = self.blti.user_first_name
        context['user_last_name'] = self.blti.user_last_name
        context['user_full_name'] = self.blti.user_full_name
        context['account_sis_id'] = account_sis_id
        context['canvas_account_id'] = self.blti.canvas_account_id
        context['course_sis_id'] = self.blti.course_sis_id
        context['course_long_name'] = self.blti.course_long_name
        context['canvas_course_id'] = self.blti.canvas_course_id
        context['is_seattle'] = account_sis_id[:16] == 'uwcourse:seattle'
        context['is_tacoma'] = account_sis_id[:15] == 'uwcourse:tacoma'
        context['is_bothell'] = account_sis_id[:16] == 'uwcourse:bothell'

        context['is_instructor'] = self.blti.is_instructor
        context['is_ta'] = self.blti.is_teaching_assistant
        context['is_student'] = self.blti.is_student
        context['is_admin'] = self.blti.is_administrator

        default_href_spec = ('https://{canvas_api_domain}' +
                             '/courses/{canvas_course_id}' +
                             '/external_tools/{{ext_id}}').format(
                                 canvas_api_domain=self.blti.canvas_api_domain,
                                 canvas_course_id=self.blti.canvas_course_id)
        external_tools = getattr(settings, "CANVAS_EXTERNAL_TOOLS", {})
        for tool in external_tools:
            confs = external_tools[tool]
            ext_context = None
            for c in confs:
                ext_context = self._external_tool_context(
                    tool, c, default_href_spec)
                if ext_context:
                    break

            if ext_context:
                context.update(ext_context)

        return context

    def _external_tool_context(self, tool, conf, default_spec):
        if ('subaccounts' in conf and
                not self._valid_subaccount(
                    self.blti.account_sis_id, conf['subaccounts'])):
            return None

        context = {}
        ext_id = conf.get('ext_id', None)
        context['{}_ext_id'.format(tool)] = ext_id
        context['{}_href'.format(tool)] = conf.get(
                'href_spec', default_spec).format(
                    ext_id=ext_id,
                    canvas_course_id=self.blti.canvas_course_id,
                    course_sis_id=self.blti.course_sis_id,
                    course_sws_id=CanvasCourse(
                        sis_course_id=self.blti.course_sis_id).sws_course_id(),
                    canvas_api_domain=self.blti.canvas_api_domain)

        return context

    def _valid_subaccount(self, account_sis_id, subaccount_sis_ids):
        for subaccount in subaccount_sis_ids:
            if subaccount[-1:] == ':':
                if subaccount == account_sis_id[:len(subaccount)]:
                    return True
            elif subaccount == account_sis_id:
                return True

        return False
