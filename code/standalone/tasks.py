# -*- coding: utf-8 -*-

from celery import Celery, task
from celery.decorators import periodic_task
from celery.task.schedules import crontab

import requests

app = Celery('tasks', broker='amqp://')


@task
def baixar_pagina(url):
    pagina = requests.get(url)

    return pagina


@periodic_task(run_every=crontab(minute='*/30'))
def baixar_varias_paginas():
    for i in range(0, 100, 10):
        baixar_pagina.delay('https://httpbin.org/links/{0}'.format(i))
