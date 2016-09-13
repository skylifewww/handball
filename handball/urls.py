from django.conf import settings
from django.conf.urls import patterns, include, url
# from django.conf.urls import include, url
from handball.views import *
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = [

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^articles/', include("article.urls")),
    url(r'contact/$',contact),
    url(r'about/$',about),
    url(r'events/$',events),
    url(r'gallery/$',gallery),

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEVELOPMENT and settings.DEBUG and 'debug_toolbar' in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)))

if settings.DEVELOPMENT or settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        url(r'^media/(?P<path>.*)$', 'serve', {'document_root': settings.MEDIA_ROOT}))
