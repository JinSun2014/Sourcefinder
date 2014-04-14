from settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db',
        'USER': 'db_user',
        'PASSWORD': 'db_pwd',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}
