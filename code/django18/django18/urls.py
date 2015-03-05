# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'', include('django18.newsletter.urls', namespace='newsletter')),
    url(r'^admin/', include(admin.site.urls)),
]
