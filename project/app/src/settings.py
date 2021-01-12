DATABASES = {
    'default' : {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME':'appdb',
        'USER': 'approot',
        'PASSWORD' : 'password',
        'HOST': 'postgres',
        'PORT':'5432
    }
}
# Static files (CSS,JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL  = '/static/'

#MEdia Files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'




