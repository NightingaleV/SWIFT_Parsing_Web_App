"""
ASGI config for SWIFT_Parsing_Web_App project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SWIFT_Parsing_Web_App.settings')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.config')
settings_module = "settings.config.production" \
    if 'WEBSITE_HOSTNAME' in os.environ else 'settings.config.local'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_asgi_application()
