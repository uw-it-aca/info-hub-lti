from blti.views import BLTILaunchView


class InfoHubView(BLTILaunchView):
    template_name = 'infohub/home.html'

    def get_context_data(self, **kwargs):
        if self.blti.course_sis_id:
            course_sis_id = self.blti.course_sis_id
        else:
            course_sis_id = 'course_{}'.format(self.blti.canvas_course_id)

        return {}
