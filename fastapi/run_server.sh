#!/bin/sh

gunicorn app:app -c config.py -k uvicorn.workers.UvicornWorker
