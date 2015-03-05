# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class Contato(models.Model):
    nome = models.CharField(max_length=90)
    email = models.EmailField()

    def __unicode__(self):
        return '{0} <{1}>'.format(self.nome, self.email)
