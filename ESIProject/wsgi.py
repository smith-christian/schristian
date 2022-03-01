"""
WSGI config for ESIProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

import socketio
import eventlet
import eventlet.wsgi

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

from sioapp.views import sio

application = get_wsgi_application()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ESIProject.settings')

django_app = StaticFilesHandler(application)
application = socketio.Middleware(sio, wsgi_app=django_app, socketio_path='socket.io')


eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 5100)), application)