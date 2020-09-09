from django.conf import settings
from django.shortcuts import redirect
from blti import BLTIException
from blti.views import BLTILaunchView, BLTIView
from blti.validators import Roles
import re


class InfoHubLaunchView(BLTILaunchView):
    def post(self, request, *args, **kwargs):
        return(redirect('infohub'))


class InfoHubView(BLTIView):
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
        context['course_long_name'] = self.blti.data.get('context_title', '')
        context['canvas_course_id'] = self.blti.canvas_course_id
        context['is_seattle'] = account_sis_id[:16] == 'uwcourse:seattle'
        context['is_tacoma'] = account_sis_id[:15] == 'uwcourse:tacoma'
        context['is_bothell'] = account_sis_id[:16] == 'uwcourse:bothell'
        try:
            Roles()._has_role(self.blti, ['Instructor'])
            context['is_instructor'] = True
        except BLTIException:
            context['is_instructor'] = False
            pass

        try:
            Roles()._has_role(self.blti, ['TeachingAssistant'])
            context['is_ta'] = True
        except BLTIException:
            context['is_ta'] = False
            pass

        try:
            Roles()._has_role(self.blti, ['Learner'])
            context['is_student'] = True
        except BLTIException:
            context['is_student'] = False
            pass

        try:
            Roles()._has_role(self.blti, ['Administrator'])
            context['is_admin'] = True
        except BLTIException:
            context['is_admin'] = False
            pass

        default_href_spec = ('/courses/{canvas_course_id}' +
                             '/external_tools/{ext_id}')
        external_tools = getattr(settings, "CANVAS_EXTERNAL_TOOLS", {})
        for tool in external_tools:
            conf = external_tools[tool]
            ext_id = conf.get('ext_id', None)

            if ('subaccounts' in conf and
                    not self._valid_subaccount(
                        account_sis_id, conf['subaccounts'])):
                continue

            context['{}_ext_id'.format(tool)] = ext_id
            context['{}_href'.format(tool)] = conf.get(
                'href_spec', default_href_spec).format(
                    ext_id=ext_id,
                    canvas_course_id=self.blti.canvas_course_id,
                    course_sis_id=self.blti.course_sis_id,
                    course_sws_id=self._sis_to_sws(self.blti.course_sis_id))

        return context

    def _valid_subaccount(self, account_sis_id, subaccount_sis_ids):
        for subaccount in subaccount_sis_ids:
            if subaccount[-1:] == ':':
                if subaccount == account_sis_id[:len(subaccount)]:
                    return True
            elif subaccount == account_sis_id:
                return True

        return False

    def _sis_to_sws(self, course_sis_id):
        m = re.match(('^([0-9]{4})-(autumn|winter|spring|summer)-' +
                      '([^-]+)-([0-9]+)-([A-Z]+)$'), course_sis_id)
        return "{year},{quarter},{curric},{course}/{section}".format(
            year=m.group(1), quarter=m.group(2), curric=m.group(3),
            course=m.group(4), section=m.group(5)) if m else ""
