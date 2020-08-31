from django.shortcuts import redirect
from blti import BLTIException
from blti.views import BLTILaunchView, BLTIView
from blti.validators import Roles


class InfoHubLaunchView(BLTILaunchView):
    def post(self, request, *args, **kwargs):
        return(redirect('infohub'))


class InfoHubView(BLTIView):
    template_name = 'infohub/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        account_sis_id = self.blti.account_sis_id
        context['user_login_id'] = self.blti.user_login_id
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

        return context
