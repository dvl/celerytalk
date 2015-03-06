# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.views.generic import FormView, TemplateView

from .forms import NewsletterForm
from .models import Contato
from .tasks import enviar_email


class IndexView(TemplateView):
    template_name = 'index.html'


class NewsletterView(FormView):
    form_class = NewsletterForm
    template_name = 'newsletter_form.html'
    initial = {
        'assunto': '%nome%, aproveite nossas ofertas!',
        'mensagem': 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.'
    }

    def form_valid(self, form):
        contatos = Contato.objects.all()

        for contato in contatos:
            enviar_email.delay(form['assunto'].value(),
                               form['mensagem'].value(),
                               contato.pk)

        return HttpResponseRedirect('/enviado/')


class NewsletterEnviadoView(TemplateView):
    template_name = 'newsletter_enviado.html'
