"""
WSGI config for telebot project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from core.bot import TranslationBot

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "telebot.settings")
# start a bot
TranslationBot().start()

application = get_wsgi_application()
