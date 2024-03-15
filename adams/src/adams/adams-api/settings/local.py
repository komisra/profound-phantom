import sys

# make sure debug is turned OFF when running in prod
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': django.db.backends.sqlite3,
        'NAME': 'Users/komalmisra/repos/profound-phantom/adams/src/adams.db'
    }
}