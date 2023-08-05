import os
import socketio
from . import settings 

from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stream_app.settings')

# create a Socket.IO server
if os.getenv('ENV') == 'DEV':
    sio = socketio.Server()
else:
    from gevent import pywsgi
    # from geventwebsocket.handler import WebSocketHandler
    
    sio = socketio.Server(
        async_mode='gevent',
        cors_allowed_origins="*",
        logger=True,
        engineio_logger=True,
        namespaces='*'
        )

application = get_wsgi_application()
application = socketio.WSGIApp(sio, application)

# pywsgi.WSGIServer(('', 8000), application, handler_class=WebSocketHandler).serve_forever()
