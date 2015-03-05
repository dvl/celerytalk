# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import forms


class NewsletterForm(forms.Form):
    assunto = forms.CharField()
    mensagem = forms.CharField(widget=forms.Textarea)
