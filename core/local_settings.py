# any local settings that change per host


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangostack',
        'HOST': '/Applications/djangostack-1.4.3-0/postgresql',
        'PORT': '5433',
        'USER': 'bitnami',
        'PASSWORD': 'eed6f63afb'
    }
}
