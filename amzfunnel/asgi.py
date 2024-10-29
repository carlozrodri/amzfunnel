"""
ASGI config for amzfunnel project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from django.urls import path
from core import consumers  # importa el consumer que crearemos

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amzfunnel.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path('ws/scrape-status/', consumers.ScrapeStatusConsumer.as_asgi()),  # ruta para el WebSocket
        ])
    ),
})