from django.conf.urls import url
import content.views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
     
    # url(r'^(?P<slug>[_0-9a-zA-Z-]+)/$', 'content.views.page', name='page'),
    # url(r'^kubok_ukr/$', content.views.plays),
    # url(r'^chemp_ukr/$', content.views.plays),
    # url(r'^force/$', content.views.force),
    # url(r'^session/$', content.views.force),
    # url(r'^sloboda/$', content.views.plays),
    # url(r'^taktic/$', content.views.force),
    # url(r'^frends_play/$', content.views.plays),
    url(r'^cat_plays/get/(?P<cat_play_id>\d+)/$', content.views.plays),
]
