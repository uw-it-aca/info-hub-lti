from .base_settings import *

INSTALLED_APPS += [
    'infohub.apps.InfohubConfig',
    'compressor',
]

RTTL_API_KEY = os.getenv('RTTL_API_KEY')
RTTL_API_URL = os.getenv('RTTL_API_URL')

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_ROOT = '/static/'

COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)

STATICFILES_FINDERS += (
    'compressor.finders.CompressorFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

COMPRESS_PRECOMPILERS += (
    ('text/x-sass', 'pyscss {infile} > {outfile}'),
    ('text/x-scss', 'pyscss {infile} > {outfile}'),
)

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter'
]
COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter',
]

DETECT_USER_AGENTS = {
    'is_tablet': False,
    'is_mobile': False,
    'is_desktop': True,
}

CANVAS_EXTERNAL_TOOLS = {
    'uw_groups': [
        {
            'ext_id': '31485'
        }
    ],
    'uw_grade_scale': [
        {
            'ext_id': '13050',
        }
    ],
    'uw_classlist': [
        {
            'ext_id': '37913',
            'subaccounts': ['uwcourse:']
        }
    ],
    'uw_panopto': [
        {
            'ext_id': '21130',
        }
    ],
    'uw_panopto_scheduler': [
        {
            'ext_id': '214645',
            'subaccounts': ['uwcourse:seattle:arts-&-sciences:']
        },
        {
            'ext_id': '214704',
            'subaccounts': ['uwcourse:seattle:education:']
        },
        {
            'ext_id': '214646',
            'subaccounts': ['uwcourse:seattle:engineering:']
        },
        {
            'ext_id': '214704',
            'subaccounts': ['uwcourse:seattle:education:']
        },
        {
            'ext_id': '214664',
            'subaccounts': ['uwcourse:seattle:information-school:']
        },
        {
            'ext_id': '214659',
            'subaccounts': ['uwcourse:seattle:medicine:']
        },
        {
            'ext_id': '214647',
            'subaccounts': ['uwcourse:seattle:public-health:']
        },
        {
            'ext_id': '214705',
            'subaccounts': ['uwcourse:seattle:interschool-or-col:']
        },
        {
            'ext_id': '214653',
            'subaccounts': ['uwcourse:seattle:environment:']
        },
        {
            'ext_id': '214669',
            'subaccounts': ['uwcourse:seattle:business-school:']
        },
        {
            'ext_id': '214661',
            'subaccounts': ['uwcourse:seattle:nursing:']
        },
        {
            'ext_id': '214654',
            'subaccounts': ['uwcourse:seattle:pharmacy:']
        },
        {
            'ext_id': '214703',
            'subaccounts': ['uwcourse:seattle:built-environments:']
        },
        {
            'ext_id': '214648',
            'subaccounts': ['uwcourse:seattle:dentistry:']
        },
        {
            'ext_id': '214656',
            'subaccounts': ['uwcourse:seattle:interdisc-graduate-progr:']
        },
        {
            'ext_id': '214699',
            'subaccounts': ['uwcourse:seattle:interdisc-undergrad-prog:']
        },
        {
            'ext_id': '214655',
            'subaccounts': ['uwcourse:seattle:law:']
        },
        {
            'ext_id': '214657',
            'subaccounts': ['uwcourse:seattle:social-work:']
        },
        {
            'ext_id': '214658',
            'subaccounts': ['uwcourse:seattle:int-col:']
        },
        {
            'ext_id': '214660',
            'subaccounts': ['uwcourse:seattle:pub-pol-&-gov:']
        },
        {
            'ext_id': '214696',
            'subaccounts': ['uwcourse:seattle:interdisc-undergrad-prog:train:']
        }
    ],
    'uw_rttlinfo': [
        {
            'ext_id': '214314',
        }
    ],
    'uw_zoom': [
        {
            'ext_id': '83805',
            'subaccounts': ['uwcourse:seattle:nursing:']
        },
        {
            'ext_id': '95443',
        },
    ],
    'uw_poll_everywhere': [
        {
            'ext_id': '41789',
        }
    ],
    'uw_accessibility': [
        {
            'ext_id': '93468',
            'subaccounts': ['uwcourse:']
        }
    ],
    'uw_add_people': [
        {
            'href_spec': 'https://{canvas_api_domain}/courses/{canvas_course_id}/users?add_people=true',
            'subaccounts': ['uwcourse:']
        }
    ],
    'uw_coda': [
        {
            'href_spec': 'https://coda.uw.edu/#{course_sis_id}',
            'subaccounts': ['uwcourse:']
        }
    ],
    'myuw_classlist': [
        {
            'href_spec': 'https://my.uw.edu/teaching/{course_sws_id}/students',
            'subaccounts': ['uwcourse:']
        }
    ]
}

if os.getenv('ENV', 'localdev') == "localdev":
    DEBUG = True
    LTI_DEVELOP_APP = os.getenv("LTI_DEVELOP_APP", '')
    if 'blti.middleware.SameSiteMiddleware' in MIDDLEWARE:
        MIDDLEWARE.remove('blti.middleware.SameSiteMiddleware')

    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
else:
    DEBUG = False
