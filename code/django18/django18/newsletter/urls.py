# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import NewsletterView, NewsletterEnviadoView, IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^form/$', NewsletterView.as_view(), name='form'),
    url(r'^enviado/$', NewsletterEnviadoView.as_view(), name='enviado'),
]
