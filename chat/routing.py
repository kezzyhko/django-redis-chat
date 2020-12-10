from django.conf.urls import url
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from . import consumers

websocket_urlpatterns = [
	url('chat/', consumers.ChatConsumer),
]

application = ProtocolTypeRouter({
	'websocket': AuthMiddlewareStack(
		URLRouter(websocket_urlpatterns)
	),
})