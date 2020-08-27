from django.conf import settings
from django.views.generic import TemplateView
from blti.views import BLTILaunchView
from time import time
from urllib.parse import quote, unquote
from oauthlib.common import generate_nonce
from oauthlib.oauth1.rfc5849 import Client
from oauthlib.oauth1.rfc5849.signature import (
    base_string_uri, signature_base_string,
    normalize_parameters, sign_hmac_sha1_with_client)


class InfoHubView(BLTILaunchView):
    template_name = 'infohub/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['user_login_id'] = self.blti.user_login_id
        context['user_full_name'] = self.blti.user_full_name
        account_sis_id = self.blti.account_sis_id
        context['is_seattle'] = account_sis_id[:16] == 'uwcourse:seattle'
        context['is_tacoma'] = account_sis_id[:15] == 'uwcourse:tacoma'
        context['is_bothell'] = account_sis_id[:16] == 'uwcourse:bothell'

        return context


class InfoHubDevPrepare(TemplateView):
    template_name = 'infohub/develop.html'


class InfoHubDevLaunch(TemplateView):
    template_name = 'infohub/launch.html'

    _lti_role = {
        'administrator': 'urn:lti:instrole:ims/lis/Administrator',
        'instructor': 'Instructor',
        'ta': 'urn:lti:role:ims/lis/TeachingAssistant',
        'student': 'Learner,'
    }

    _lti_ext_role = {
        'administrator': 'urn:lti:instrole:ims/lis/Administrator,urn:lti:instrole:ims/lis/Instructor,urn:lti:instrole:ims/lis/Student,urn:lti:role:ims/lis/Learner,urn:lti:role:ims/lis/Learner/NonCreditLearner,urn:lti:role:ims/lis/Mentor,urn:lti:sysrole:ims/lis/Useurn:lti:instrole:ims/lis/Administrator,urn:lti:instrole:ims/lis/Instructor,urn:lti:instrole:ims/lis/Student,urn:lti:role:ims/lis/Learner,urn:lti:role:ims/lis/Learner/NonCreditLearner,urn:lti:role:ims/lis/Mentor,urn:lti:sysrole:ims/lis/User',
        'instructor': 'urn:lti:instrole:ims/lis/Instructor,urn:lti:instrole:ims/lis/Student,urn:lti:role:ims/lis/Instructor,urn:lti:sysrole:ims/lis/User',
        'ta': 'urn:lti:instrole:ims/lis/Instructor,urn:lti:instrole:ims/lis/Student,urn:lti:role:ims/lis/Instructor,urn:lti:role:ims/lis/TeachingAssistant,urn:lti:sysrole:ims/lis/User',
        'student': 'urn:lti:instrole:ims/lis/Student,urn:lti:role:ims/lis/Learner,urn:lti:sysrole:ims/lis/User'
    }

    _static_lti_parameters = [
        ("oauth_consumer_key", "0000-0000-0000"),
        ("oauth_signature_method", "HMAC-SHA1"),
        ("oauth_version", "1.0"),
        ("context_id", "3F2DcDcF6aCBef17a2eccCDdA498e9e5Cc333A96"),
        ("context_label", "PSYCH 101 A"),
        ("context_title", "PSYCH 101 A Au 19: Introduction To Psychology"),
        ("custom_application_type", "UWInfoHub"),
        ("custom_canvas_account_id", "8675309"),
        ("custom_canvas_api_domain", "uw.test.instructure.com"),
        ("custom_canvas_course_id", "88675309"),
        ("custom_canvas_enrollment_state", "active"),
        ("custom_canvas_user_id", "700007"),
        ("custom_canvas_user_login_id", "javerage"),
        ("custom_canvas_workflow_state", "available"),
        ("launch_presentation_document_target", "iframe"),
        ("launch_presentation_height", "400"),
        ("launch_presentation_locale", "en"),
        ("launch_presentation_width", "800"),
        ("lis_course_offering_sourcedid", "2019-autumn-PSYCH-101-A"),
        ("lis_person_contact_email_primary", "javerage@u.washington.edu"),
        ("lis_person_name_family", "Average"),
        ("lis_person_name_full", "James Average"),
        ("lis_person_name_given", "James"),
        ("lis_person_sourcedid", "0C8F043FA5CBE23F2B1E1A63B1BD80B8"),
        ("lti_message_type", "basic-lti-launch-request"),
        ("lti_version", "LTI-1p0"),
        ("oauth_callback", "about:blank"),
        ("resource_link_id", "E9a206DC909a330e9F8eF183b7BB4B9718aBB62d"),
        ("resource_link_title", "UW Info Hub"),
        ("tool_consumer_info_product_family_code", "canvas"),
        ("tool_consumer_instance_name", "University of Washington"),
        ("user_id", "e1ec31bd10a32f61dd65975ce4eb98e9f106bd7d"),
        ("user_image", "/images/thumbnails/1499380/24ZSCuR73P2mrG98Yq6gicMHjcd0p8NMhM2iGhgz"),
    ]

    def get_context_data(self, **kwargs):
        role = self.request.GET.get('role', '')
        campus = self.request.GET.get('campus', '')

        lti_parameters = []
        lti_parameters.append(("roles", quote(self._lti_role[role])))
        lti_parameters.append(("ext_roles", quote(self._lti_ext_role[role])))
        lti_parameters.append((
            "custom_canvas_account_sis_id",
            'uwcourse:{}:arts-&-sciences:psych:psych'.format(campus)))
        lti_parameters.append(("oauth_timestamp", str(int(time()))))
        lti_parameters.append(("oauth_nonce", generate_nonce()))
        lti_parameters += self._static_lti_parameters


        # calculate signature
        raw_uri = self.request.build_absolute_uri()
        uri = raw_uri[0:raw_uri.index('/infohub') + 8]
        sbs = signature_base_string(
            'POST', base_string_uri(uri), normalize_parameters(lti_parameters))
        client_key = '0000-0000-0000'
        client_secrets = getattr(settings, 'LTI_CONSUMERS', {})
        client = Client(client_key, client_secret=client_secrets[client_key])
        signature = sign_hmac_sha1_with_client(sbs, client)
        lti_parameters.append(("oauth_signature", signature))

        context = super().get_context_data(**kwargs)
        context['uri'] = uri
        context['campus'] = campus
        context['role_name'] = role
        context['lti_parameters'] = lti_parameters
        return context
