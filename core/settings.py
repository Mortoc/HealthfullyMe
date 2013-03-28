import dj_database_url
import os, sys
import socket

try:
    HOSTNAME = socket.gethostname()
    if ".local" in HOSTNAME:
        raise "Shouldn't use the weird mac localhost naming thing"
except:
    HOSTNAME = 'localhost:8000'

LIVE = False # dev == False, live == True
TEST = 'test' in sys.argv

if os.environ.get('HEALTHFULLY_ME_DEPLOYMENT', "none") == "LIVE":
    LIVE = True
elif os.environ.get('HEALTHFULLY_ME_DEPLOYMENT', "none") == "DEV":
    LIVE = False
else:
    raise Exception("HEALTHFULLY_ME_DEPLOYMENT hasn't been set on this machine")
    

DEBUG = True
TEMPLATE_DEBUG = DEBUG

BASE_DIR = os.path.dirname( os.path.abspath(__file__) )

if TEST:
    DATABASES = { 'default' : {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': 'test_db'
                    }
                }
else:
    # Parse database configuration from $DATABASE_URL
    DATABASES = { 
        'default' : dj_database_url.config(
            default="postgres://postgres:cab8dixo@localhost/healthfullyme_local"
        ) 
    }

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Stripe
if not LIVE:
    # Test Key
    STRIPE_SECRET_KEY = "sk_test_qxHGPxPMzqErH3QWxjhcDhCo"
    STRIPE_PUBLIC_KEY = "pk_test_1Kp5hj2mMh26L6eRJBbz1Kb3"
else:
    # Live Key
    STRIPE_SECRET_KEY = "sk_live_NsfXzNtk6iBhh8Nn8pXhKU7j"
    STRIPE_PUBLIC_KEY = "pk_live_U7o0baBYeO20Ex4bKaOlphC8"


# Segment.io
if not LIVE:
    #dev
    SEGMENT_IO_KEY = "34t4a37fwy"
else:
    #live
    SEGMENT_IO_KEY = "hspdwym69u"


ADMINS = (
    ('Mortoc', 'Mortoc@healthfully.me'),
)

MANAGERS = ADMINS


# Email settings
EMAIL_HOST = "smtp.sendgrid.net"
EMAIL_HOST_USER = "mortoc"
EMAIL_HOST_PASSWORD = "cab8dixo"
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, '../static_compiled/')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

SOUTH_TESTS_MIGRATE = False

AUTH_USER_MODEL = 'core.HMUser'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../core/static'),
    os.path.join(BASE_DIR, '../home/static'),
    os.path.join(BASE_DIR, '../store/static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '@huwrgdpurvt)ps534p;pb#7!e0ifr_i!0ergoe&amp;46x%^u0(&amp;u12si'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    #"django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "core.context_processors.config_data"
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'core.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'core.wsgi.application'

TEMPLATE_DIRS = (
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    
    'django_extensions',
    'gunicorn',
    'south',
    
    'home',
    'giftcards',
    'store',
    'core'
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
