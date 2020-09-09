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

if os.getenv('ENV', 'localdev') == "localdev":
    DEBUG = True
    LTI_DEVELOP_APP = os.getenv("LTI_DEVELOP_APP", '')
    if 'blti.middleware.SameSiteMiddleware' in MIDDLEWARE:
        MIDDLEWARE.remove('blti.middleware.SameSiteMiddleware')

    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
else:
    DEBUG = False
