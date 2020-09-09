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
    'uw_groups': {
        'ext_id': '31485'
    },
    'uw_grade_scale': {
        'ext_id': '13050',
    },
    'uw_classlist': {
        'ext_id': '37913',
        'subaccounts': ['uwcourse:']
    },
    'uw_accessibility': {
        'ext_id': '37913',
        'subaccounts': ['uwcourse:']
    },
    'uw_coda': {
        'href_spec': 'https://coda.uw.edu/#{course_sis_id}',
        'subaccounts': ['uwcourse:']
    },
    'myuw_classlist': {
        'href_spec': 'https://my.uw.edu/teaching/{course_sws_id}/students',
        'subaccounts': ['uwcourse:']
    }
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
