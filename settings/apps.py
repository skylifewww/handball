INSTALLED_APPS = (
    'grappelli',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',

    # libs
    'authtools',
    'django_extensions',
    'easy_thumbnails',
    'mptt',
    'storages',
    'boto',
    'social.apps.django_app.default',
    'embed_video',
    'ckeditor',
    'ckeditor_uploader',

    # apps
    'handball.core',
    'handball.users',
    'article',
    # 'about',
    'content',
)
