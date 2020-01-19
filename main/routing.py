# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.conf.urls import url
# from channels.auth import AuthMiddlewareStack
# from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

# from chat.consumers import ChatConsumer

# application = ProtocolTypeRouter({
#     # Empty for now (http->django views is added by default)
#     'websocket': AllowedHostsOriginValidator(
#         AuthMiddlewareStack(
#             URLRouter(
#                 # url(r"^messages/(?P<username>[\w.@+-]+)/$", ChatConsumer),
#             )
#         )
#     )
# })

# from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from django.conf.urls import url

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})

