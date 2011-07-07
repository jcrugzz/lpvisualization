from django.conf.urls.defaults import *

handler500 = 'djangotoolbox.errorviews.server_error'

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	('^_ah/warmup$', 'djangoappengine.views.warmup'),
	('^lpVis/$', 'lpVis.views.lp_listing'),
	url('^admin/', include(admin.site.urls)),
)
