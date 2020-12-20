import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd@33nlnf9h@*a#pcont%ow^%6r%3k^*q=id(v3z#syvt!36)m2'

# SECURITY WARNING: don't run with debug turned on in production!
import os.path
DEBUG = os.path.isfile('DEBUG') # there will be no file 'DEBUG' on github and inside docker containers

ALLOWED_HOSTS = ['*']

SESSION_COOKIE_HTTPONLY = False


# Application definition

INSTALLED_APPS = [
	'chat',
	'channels',
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'whitenoise.middleware.WhiteNoiseMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'chat.urls'

ROOT_HOSTCONF = 'chat.hosts'

DEFAULT_HOST = 'default'

PARENT_HOST = 'localhost'

HOST_PORT = '8000'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, 'templates')],
		# 'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
			'loaders': [
				'django.template.loaders.filesystem.Loader',
				'django.template.loaders.app_directories.Loader',
			],
		},
	},
]

WSGI_APPLICATION = 'chat.wsgi.application'


# Channels

ASGI_APPLICATION = "chat.routing.application"

CHANNEL_LAYERS = {
	'default': {
		'BACKEND': 'channels_redis.core.RedisChannelLayer',
		'CONFIG': {
			"hosts": [(os.environ.get('REDIS', 'redis'), 6379)],
		},
	},
}


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'postgres',
		'USER': 'postgres',
		'PASSWORD': 'postgres',
		'HOST': os.environ.get('POSTGRES', 'postgres'),
		'PORT': 5432,
	},
}

DATABASE_ROUTERS = ['chat.routers.DatabaseAppsRouter']

DATABASE_APPS_MAPPING = {
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
	{
		'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
	},
]

AUTH_USER_MODEL = 'chat.HostsAuthUser'
AUTH_PROFILE_MODULE = 'chat.HostsAuthUser'

AUTHENTICATION_BACKENDS = (
	'chat.backends.HostsAuthBackend',
	# 'django.contrib.auth.backends.ModelBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
	os.path.join(BASE_DIR, "static"),
]

STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_URL = '/media/'

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'formatters': {
		'default': {
			'format': '[DJANGO] %(levelname)s %(asctime)s %(module)s '
					  '%(name)s.%(funcName)s:%(lineno)s: %(message)s'
		},
	},
	'handlers': {
		'console': {
			'level': 'DEBUG',
			'class': 'logging.StreamHandler',
			'formatter': 'default',
		}
	},
	'loggers': {
		'*': {
			'handlers': ['console'],
			'level': 'DEBUG',
			'propagate': True,
		},
	},
}