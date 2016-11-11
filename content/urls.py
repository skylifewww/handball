from django.conf.urls import url
import content.views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    url(r'^$', content.views.raspisanie),
    url(r'^force/$', content.views.force),
    url(r'^cat_plays/get/(?P<cat_play_id>\d+)/$', content.views.plays),
]
