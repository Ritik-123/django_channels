import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from myapp.router import websocket_urlpatterns
import myapp.router

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')


application= ProtocolTypeRouter(
    {
        'http': get_asgi_application(),
        'websocket': AuthMiddlewareStack(
            URLRouter(
                myapp.router.websocket_urlpatterns
                # websocket_urlpatterns
                )
            ) 
    }
)

# application = get_asgi_application()
# application= ProtocolTypeRouter({
#     'http': get_asgi_application(),
#     'websocket': AllowedHostsOriginValidator(
#         AuthMiddlewareStack(
#             URLRouter(
#                 websocket_urlpatterns
#             )
#         )
#     ),
# })