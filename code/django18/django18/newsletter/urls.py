# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import NewsletterView, NewsletterEnviadoView

urlpatterns = [
    url(r'^form/$', NewsletterView.as_view(), name='form'),
    url(r'^enviado/$', NewsletterEnviadoView.as_view(), name='enviado'),
]
