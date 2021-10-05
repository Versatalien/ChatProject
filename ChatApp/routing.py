from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
import ChatApp.apps.chat.routing

application = ProtocolTypeRouter({
"websocket": AuthMiddlewareStack(URLRouter(ChatApp.apps.chat.routing.websocket_urlpatterns)),
})