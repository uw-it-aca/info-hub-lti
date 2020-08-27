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
              MIDDLEWARE +\
              ['userservice.user.UserServiceMiddleware',]

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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'stdout_stream': {
            '()': 'django.utils.log.CallbackFilter',
            'callback': lambda record: record.levelno < logging.WARN
        },
        'stderr_stream': {
            '()': 'django.utils.log.CallbackFilter',
            'callback': lambda record: record.levelno > logging.INFO
        }
    },
    'formatters': {
    },
    'handlers': {
        'stdout': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'filters': ['stdout_stream']
        },
        'stderr': {
            'class': 'logging.StreamHandler',
            'stream': sys.stderr,
            'filters': ['stderr_stream']
        },
    },
    'loggers': {
        'oauthlib': {
            'handlers': ['stdout', 'stderr'],
        },
        '': {
            'handlers': ['stdout', 'stderr'],
            'level': 'INFO' if os.getenv('ENV', 'dev') == 'prod' else 'DEBUG'
        }
    }
}


# BLTI consumer key:secret pairs in env as "k1=val1,k2=val2"
LTI_CONSUMERS = json.loads(os.getenv("LTI_CONSUMERS", "{}"))
LTI_ENFORCE_SSL=False

# BLTI session object encryption values
BLTI_AES_KEY = bytes(os.getenv('BLTI_AES_KEY', ''), encoding='utf8')
BLTI_AES_IV = bytes(os.getenv('BLTI_AES_IV', ''), encoding='utf8')

DEBUG = True if os.getenv('ENV', 'localdev') == "localdev" else False
