#archivo que nos permite cambiar ciertos parametros por su informacion contenida
from pathlib import Path
import os
######################################################################################3
# import os es una declaración en Python que importa el módulo os. El módulo os 
# proporciona funciones para interactuar con el sistema operativo en el que se 
# ejecuta Python. Al importar este módulo, puedes acceder a varias funciones y 
# métodos que te permiten realizar tareas relacionadas con el sistema operativo, 
# como la manipulación de archivos, la navegación por directorios, la obtención 
# de variables de entorno y mucho más.
#######################################################################################
import environ #modulo para proteger cosas 
env= environ.Env()#crear variables
environ.Env.read_env()#leer variables
##################################################################################### 
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent#hace referencia al directorio del archivo django
#path (file)= llama al folder core
#resolve()es un metodo que obtiene y que obtiene toda nuestra carpeta con .parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
#este se va a proteger contra los hackers
SECRET_KEY = os.environ.get('SECRET_KEY')
#################################
#IMPORTANTE PARA SEGURIDAD
#################################
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG')
#hosting con los que puede trabajar son todos y se le coloca la estrellita *
ALLOWED_HOSTS = ['*']


# Application definition
#installed apps= son como extensiones de mi aplicacion  que algunas que ya vienen pre instaladas y otras que debemos instalar 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',#se le coloca core para que django tenga acceso a todos los archivos que hay en el folder
    'blog',
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

ROOT_URLCONF = 'core.urls'

#para hacer que las cosas estan bonitas 
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
            
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
#WSGI (Web Server Gateway Interface) es una especificación para la comunicación 
# entre servidores web y aplicaciones web o frameworks en el lenguaje de programación Python. 
# Permite que las aplicaciones web escritas en Python se comuniquen de manera eficiente y 
# estandarizada con diversos servidores web  
WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
#validar las contraseñas 
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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
