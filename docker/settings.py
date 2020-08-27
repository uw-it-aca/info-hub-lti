from .base_settings import *
import json

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'compressor',
    'blti',
    'infohub',
]

MIDDLEWARE = ['blti.middleware.SessionHeaderMiddleware',
              'blti.middleware.CSRFHeaderMiddleware',] +\
              MIDDLEWARE

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

# BLTI consumer key:secret pairs in env as "k1=val1,k2=val2"
LTI_CONSUMERS = json.loads(os.getenv("LTI_CONSUMERS", "{}"))
LTI_ENFORCE_SSL=False

# BLTI session object encryption values
BLTI_AES_KEY = bytes(os.getenv('BLTI_AES_KEY', ''), encoding='utf8')
BLTI_AES_IV = bytes(os.getenv('BLTI_AES_IV', ''), encoding='utf8')

DEBUG = True if os.getenv('ENV', 'localdev') == "localdev" else False
