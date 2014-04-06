from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
import grappelli
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shopping.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    url(r'^admin', include(admin.site.urls)),
    url(r'^', include('trialshop.urls', namespace="trialshop")),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
