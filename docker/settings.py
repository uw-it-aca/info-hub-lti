from .base_settings import *

INSTALLED_APPS += [
    'compressor',
    'infohub',
]

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
            'ext_id': '25694',
            'subaccounts': ['uwcourse:seattle:arts-&-sciences:']
        },
        {
            'ext_id': '25697',
            'subaccounts': ['uwcourse:seattle:education:']
        },
        {
            'ext_id': '25698',
            'subaccounts': ['uwcourse:seattle:education:']
        },
        {
            'ext_id': '25700',
            'subaccounts': ['uwcourse:seattle:information-school:']
        },
        {
            'ext_id': '25705',
            'subaccounts': ['uwcourse:seattle:medicine:']
        },
        {
            'ext_id': '25708',
            'subaccounts': ['uwcourse:seattle:public-health:']
        },
        {
            'ext_id': '25703',
            'subaccounts': ['uwcourse:seattle:interschool-or-col:']
        },
        {
            'ext_id': '25699',
            'subaccounts': ['uwcourse:seattle:environment:']
        },
        {
            'ext_id': '23909',
            'subaccounts': ['uwcourse:seattle:business-school:']
        },
        {
            'ext_id': '25706',
            'subaccounts': ['uwcourse:seattle:nursing:']
        },
        {
            'ext_id': '25707',
            'subaccounts': ['uwcourse:seattle:pharmacy:']
        },
        {
            'ext_id': '25695',
            'subaccounts': ['uwcourse:seattle:built-environments:']
        },
        {
            'ext_id': '25696',
            'subaccounts': ['uwcourse:seattle:dentistry:']
        },
        {
            'ext_id': '25702',
            'subaccounts': ['uwcourse:seattle:interdisc-graduate-progr:']
        },
        {
            'ext_id': '25704',
            'subaccounts': ['uwcourse:seattle:law:']
        },
        {
            'ext_id': '25710',
            'subaccounts': ['uwcourse:seattle:social-work:']
        },
        {
            'ext_id': '25701',
            'subaccounts': ['uwcourse:seattle:int-col:']
        },
        {
            'ext_id': '25709',
            'subaccounts': ['uwcourse:seattle:pub-pol-&-gov:']
        },
        {
            'ext_id': '44317',
            'subaccounts': ['uwcourse:seattle:interdisc-undergrad-prog:train:']
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
