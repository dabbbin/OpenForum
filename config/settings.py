from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-l4cb@9=a!s8)6h-re)08%!04f6a%%^42kl0(t)yk6n7ngq7m_r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['43.202.81.190']


# Application definition

INSTALLED_APPS = [
    #pybo/apps.py 파일에 있는 클래스로, pybo 앱 생성 시, 자동으로 만들어지는 
    #파일을 따로 만들 필요가 없다. 이미 apps.py에 클래스가 구현되어 있다. 
    #로그인, 로그아웃 등 공통되는 기능 종속한 앱 등록
    'common.apps.CommonConfig',
    'pybo.apps.PyboConfig',
    'django.contrib.admin', 
    'django.contrib.auth',  
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], #템플릿 파일을 저장할 디렉터리 생성
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3', # = C:\projects\mysite
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

#en-us  -> ko-kr
LANGUAGE_CODE = 'ko-kr'

#UTC -> Asia/Seoul
TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [ #리스트 변수 추가
    BASE_DIR / 'static', #스타일시트 파일, 스태틱 디렉터리에 저장
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#로그인 성공 후 이동하는 URL
LOGIN_REDIRECT_URL='/'

#로그아웃 성공 후 이동하는 URL
LOGOUT_REDIRECT_URL='/'

LOGGING = {
    'version' : 1, 
    'disable_existing_loggers' : False, 
    'handlers' : {
        'console' : {
            'level' : 'DEBUG',
            'class' : 'logging.StreamHandler',
        }
    },
    'loggers' : {
        'django.db.backends' : {
            'handlers' : ['console'],
            'level' : 'DEBUG', 
        }
    }
}