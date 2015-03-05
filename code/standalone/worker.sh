#!/bin/bash

celery -A tasks --loglevel=info worker
