# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.views.generic import FormView, TemplateView

from .forms import NewsletterForm
from .models import Contato
# from .tasks import enviar_email


class NewsletterView(FormView):
    form_class = NewsletterForm
    template_name = 'newsletter_form.html'

    def form_valid(self, form):
        contatos = Contato.objects.all()

        for contato in contatos:
            send_mail(
                subject=form['assunto'],
                message=form['mensagem'],
                from_email='no-reply@xdvl.info',
                recipient_list=list(contato),
                fail_silently=False
            )

            # enviar_email.delay(form['assunto'], form['mensagem'], contato)

        return HttpResponseRedirect('/sucesso/')



class NewsletterEnviadoView(TemplateView):
    template_name = 'newsletter_enviado.html'
