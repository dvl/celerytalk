# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.mail import send_mail

from celery import shared_task

from .models import Contato


@shared_task
def enviar_email(assunto, mensagem, contato_pk):
    contato = Contato.objects.get(pk=contato_pk)

    send_mail(
        subject=assunto.replace('%nome%', contato.nome),
        message=mensagem,
        from_email='no-reply@xdvl.info',
        recipient_list=[contato.email],
        fail_silently=False
    )
