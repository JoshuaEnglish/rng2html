from bottle import request, Bottle, abort
app = Bottle()

@app.route('/')
def index():
    return '''<!DOCTYPE html>
<html>
<head>
  <script type="text/javascript">
    var ws = new WebSocket("ws://example.com:8080/websocket");
    ws.onopen = function() {
        ws.send("Hello, world");
    };
    ws.onmessage = function (evt) {
        alert(evt.data);
    };
  </script>
</head>
</html>'''

@app.route('/websocket')
def handle_websocket():
    wsock = request.environ.get('wsgi.websocket')
    if not wsock:
        abort(400, 'Expected WebSocket request.')

    while True:
        try:
            message = wsock.receive()
            wsock.send("Your message was: %r" % message)
        except WebSocketError:
            break

from gevent.pywsgi import WSGIServer
#from geventwebsocket import WebSocketError
from geventwebsocket.handler import WebSocketHandler
server = WSGIServer(("0.0.0.0", 8080), app,
                    handler_class=WebSocketHandler)
server.serve_forever()