from celery import Celery
import requests

app = Celery('tasks', broker='redis://')


@app.task
def baixar_pagina(url):
    pagina = requests.get(url)

    return pagina
