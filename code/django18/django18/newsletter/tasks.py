# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.mail import send_mail

from celery import shared_task


@shared_task
def enviar_email(assunto, mensagem, destinatario):
    send_mail(
        subject=assunto,
        message=mensagem,
        from_email='no-reply@xdvl.info',
        recipient_list=list(destinatario),
        fail_silently=False
    )
