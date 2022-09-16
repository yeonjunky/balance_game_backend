from pathlib import Path

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'balance_game',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306',

        'TEST': {
            'mirror': 'test'

        },

        'test.sqlite3': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'test.sqlite3'
        }
    },
}
