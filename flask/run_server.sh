#!/bin/sh

#gunicorn --log-level info --log-file=/gunicorn.log --workers 4 --name app -b 0.0.0.0:8000 --reload app.app:app
gunicorn -c config.py app:app 